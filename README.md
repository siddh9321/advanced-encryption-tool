# 🔐 Advanced Encryption Tool

A robust and user-friendly file encryption application built using **Python**, implementing **AES-256 and RSA Hybrid Encryption** for secure data protection.

---

## 🚀 Features

* 🔐 **AES-256 Encryption & Decryption**
* 🔑 **Hybrid Encryption (AES + RSA)**
* 👤 **Login & Register System (SQLite आधारित)**
* 🧾 **File Integrity Check (SHA-256 Hashing)**
* 🖱️ **Drag & Drop User Interface**
* ☁️ **Cloud Storage Integration (Firebase)**
* 🔑 **Key Export / Import (RSA Keys)**

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* TkinterDnD2 (Drag & Drop)
* Cryptography Library
* SQLite3 (Authentication)
* Firebase Admin SDK (Cloud Storage)

---

## 📂 Project Structure

```
Advanced_encryption_tool/
│── main.py
│── firebase_key.json (Not included in repo)
│── .gitignore
│
├── ui/
│   │── login_ui.py
│   │── app_ui.py
│
├── core/
│   │── aes_crypto.py
│   │── rsa_crypto.py
│   │── hybrid_crypto.py
│
├── utils/
│   │── file_handler.py
│   │── hash_checker.py
│   │── key_manager.py
│
├── auth/
│   │── auth_system.py
│
├── cloud/
│   │── firebase.py
│
├── screenshots/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/advanced-encryption-tool.git
cd advanced-encryption-tool
```

### 2️⃣ Install Dependencies

```
pip install cryptography
pip install tkinterdnd2
pip install firebase-admin
```

### 3️⃣ Firebase Setup (Important)

1. Go to Firebase Console
2. Create a project
3. Enable Storage
4. Go to Project Settings → Service Accounts
5. Generate a private key
6. Rename it to:

```
firebase_key.json
```

7. Place it in the root directory

---

## ▶️ Run the Application

```
python main.py
```

---

## 📸 Screenshots

> Add your screenshots inside the `screenshots/` folder

* Login Page
* Main UI
* Encryption Process
* Decryption Result
* Drag & Drop Feature

---

## 🔒 Security Note

* ❌ Do NOT upload `firebase_key.json` to GitHub
* ✔ Use `.gitignore` to protect sensitive credentials

---

## 💡 Future Improvements

* 🌙 Dark Mode UI
* 📊 Activity Logging System
* 🔗 Secure File Sharing
* 👥 Multi-user Cloud Access

---

## 📌 Project Description (For Resume)

Developed a secure file encryption tool using AES-256 and RSA hybrid encryption with features like user authentication, file integrity verification, drag-and-drop interface, cloud integration, and key management.

---

## 👨‍💻 Author

**Siddhesh Bhandari**
B.Sc. IT Student | Aspiring Cybersecurity Professional

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
