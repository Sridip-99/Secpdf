import os
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime
import uuid
from django.conf import settings  # <-- add this

def generate_unique_filename(prefix):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = uuid.uuid4().hex
    return f"{prefix}_{timestamp}_{unique_id}.pdf"

def encrypt_pdf(input_file_path, password):
    try:
        reader = PdfReader(input_file_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        output_filename = generate_unique_filename("encrypted_output")
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
        with open(output_path, "wb") as f:
            writer.write(f)

        return output_path
    except Exception as e:
        raise Exception(f"Encryption failed: {e}")

def decrypt_pdf(input_file_path, password):
    try:
        reader = PdfReader(input_file_path)

        if reader.is_encrypted:
            if not reader.decrypt(password):
                raise Exception("Wrong password or decryption failed.")
        else:
            raise Exception("The file is not encrypted.")

        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        output_filename = generate_unique_filename("decrypted_output")
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)
        with open(output_path, "wb") as f:
            writer.write(f)

        return output_path
    except Exception as e:
        raise Exception(f"Decryption failed: {e}")
