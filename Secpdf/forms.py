from django import forms

class PDFEncryptForm(forms.Form):
    pdf = forms.FileField(label="Upload PDF to Encrypt")
    password = forms.CharField(widget=forms.PasswordInput, label="Encryption Password")

class PDFDecryptForm(forms.Form):
    pdf = forms.FileField(label="Upload PDF to Decrypt")
    password = forms.CharField(widget=forms.PasswordInput, label="Decryption Password")
