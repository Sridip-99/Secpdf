# 🔒 Secure PDF Encrypt & Decrypt Web App

A Django-based responsive web application hosted on Render that allows users to **securely encrypt** and **decrypt PDF files** using a password. Files are uploaded, processed, and returned with a clean interface and security-focused logic.
Live: https://securepdf-np2x.onrender.com
Project Report: https://shorturl.at/VG48L
---

## 📸 Demo Screenshots

> *HOME PAGE IN LIGHT & DARK MODE*
![HOME PAGE IN LIGHT MODE](https://raw.githubusercontent.com/Sridip-99/Secpdf/refs/heads/main/Snapshot/home_light.png "This is a sample image.")
![HOME PAGE IN DARK MODE](https://raw.githubusercontent.com/Sridip-99/Secpdf/refs/heads/main/Snapshot/home_dark.png "This is a sample image.")

> *ENCRYPT PAGE IN DARK MODE*
![ENCRYPT PAGE IN DARK MODE](https://raw.githubusercontent.com/Sridip-99/Secpdf/refs/heads/main/Snapshot/encrypt_dark.png "This is a sample image.")

> *DECRYPT PAGE IN LIGHT MODE*
![DECRYPT PAGE IN LIGHT MODE](https://raw.githubusercontent.com/Sridip-99/Secpdf/refs/heads/main/Snapshot/decrypt_light.png "This is a sample image.")

> *RESPONSE PAGE IN LIGHT & DARK MODE*
![RESPONSE PAGE IN LIGHT MODE](https://raw.githubusercontent.com/Sridip-99/Secpdf/refs/heads/main/Snapshot/response_light.png "This is a sample image.")
![RESPONSE PAGE IN DARK MODE](https://raw.githubusercontent.com/Sridip-99/Secpdf/refs/heads/main/Snapshot/response_dark.png "This is a sample image.")

---

## ⚙️ Features

- 🔐 **Encrypt PDF** with user-defined password  
- 🔓 **Decrypt PDF** using correct password  
- 📁 **Secure File Uploads** stored in `media/`  
- 🧹 **Auto-clean** temporary uploads  
- 🧠 Smart error handling (e.g. double-encryption attempts)  
- ✅ Custom response page with download link  
- 📆 Timestamped filenames to prevent overwriting  
- 📦 Deployable & production-ready  

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **PDF Handling**: PyPDF2
- **Frontend**: HTML5, CSS3, JavaScript (minimal)
- **Storage**: FileSystem (`MEDIA_ROOT`)
- **Deployment Ready**: Gunicorn + Nginx compatible

---

## 📂 Project Structure

```bash
Secpdf/
├── Secpdf/
│   ├── views.py
│   ├── urls.py
│   ├── settings.py
│   ├── forms.py
│   └── utils.py (Core logic here)
├── templates/
│   └──error/
│     ├── 404.html
│     └── 500.html
│   ├── Index.html
│   ├── encrypt.html
│   ├── decrypt.html
│   └── response.html
├── static/
│   └── (CSS/JS/logo files)
├── media/
│   └── (output PDFs saved here)
└── manage.py
