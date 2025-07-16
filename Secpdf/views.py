import os
import uuid
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib import messages
from .forms import PDFEncryptForm, PDFDecryptForm
from .utils import encrypt_pdf, decrypt_pdf


# ──────────────────────────── Utility ───────────────────────────── #

def save_uploaded_file(uploaded_file, sub_dir='uploaded_pdfs'):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    original_name = slugify(uploaded_file.name.rsplit('.', 1)[0])
    unique_name = f"{original_name}_{timestamp}_{uuid.uuid4().hex}.pdf"

    upload_dir = os.path.join(settings.MEDIA_ROOT, sub_dir)
    fs = FileSystemStorage(location=upload_dir)
    saved_path = fs.save(unique_name, uploaded_file)
    full_path = os.path.join(upload_dir, saved_path)

    return full_path


def delete_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)


# ──────────────────────────── Page Views ───────────────────────────── #

def custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_server_error_view(request):
    return render(request, 'errors/500.html', status=500)

def homePage(request):
    return render(request, "Index.html", {'title': 'Secure PDF'})

def encrypt(request):
    return render(request, "encrypt.html", {'title': 'Encrypt PDF'})

def decrypt(request):
    return render(request, "decrypt.html", {'title': 'Decrypt PDF'})

def response(request):
    file_url = request.session.get('file_path')
    return render(request, 'response.html', {'title': 'Response', 'file_url': file_url})


# ──────────────────────────── Core Logic ───────────────────────────── #

def encrypt_file(request):
    if request.method == 'POST':
        form = PDFEncryptForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pdf = form.cleaned_data['pdf']
                password = form.cleaned_data['password']

                full_input_path = save_uploaded_file(pdf)

                output_path = encrypt_pdf(full_input_path, password)

                if not os.path.exists(output_path):
                    messages.error(request, "Encryption failed: Output file not created.")
                    return render(request, 'encrypt.html', {'form': form, 'title': 'Encrypt PDF'})

                # Clean original upload
                delete_file_if_exists(full_input_path)

                request.session['file_path'] = os.path.join('/media/', os.path.basename(output_path))
                messages.success(request, "PDF encrypted successfully!")
                return redirect('response')

            except Exception as e:
                if "File has not been decrypted" in str(e):
                    messages.error(request, "This file is already encrypted. Please upload an unencrypted PDF.")
                else:
                    messages.error(request, f"Error during encryption: {e}")
        else:
            messages.error(request, "Invalid form data. Please try again.")
    else:
        form = PDFEncryptForm()

    return render(request, 'encrypt.html', {'form': form, 'title': 'Encrypt PDF'})


def decrypt_file(request):
    if request.method == 'POST':
        form = PDFDecryptForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                pdf = form.cleaned_data['pdf']
                password = form.cleaned_data['password']

                full_input_path = save_uploaded_file(pdf)

                output_path = decrypt_pdf(full_input_path, password)

                if not os.path.exists(output_path):
                    messages.error(request, "Decryption failed: Output file not created.")
                    return render(request, 'decrypt.html', {'form': form, 'title': 'Decrypt PDF'})
                
                delete_file_if_exists(full_input_path)

                request.session['file_path'] = os.path.join('/media/', os.path.basename(output_path))
                messages.success(request, "PDF decrypted successfully!")
                return redirect('response')

            except Exception as e:
                messages.error(request, f"Error during decryption: {e}")
        else:
            messages.error(request, "Invalid form data. Please try again.")
    else:
        form = PDFDecryptForm()

    return render(request, 'decrypt.html', {'form': form, 'title': 'Decrypt PDF'})
