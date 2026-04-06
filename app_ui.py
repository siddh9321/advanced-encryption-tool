import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD

from core.hybrid_crypto import hybrid_encrypt, hybrid_decrypt
from core.rsa_crypto import generate_keys
from utils.file_handler import read_file, write_file
from utils.hash_checker import get_hash

# 🔥 NEW IMPORTS
from cloud.firebase import upload_file, download_file
from utils.key_manager import save_private_key, save_public_key, load_private_key, load_public_key

# Generate keys
private_key, public_key = generate_keys()

def launch_main_app():
    global private_key, public_key

    app = TkinterDnD.Tk()
    app.title("Advanced Encryption Tool")
    app.geometry("450x450")

    selected_file = {"path": None}

    # 📂 Drag & Drop
    def drop(event):
        file_path = event.data.strip("{}")
        selected_file["path"] = file_path
        label.config(text=f"Selected: {file_path}")

    def browse_file():
        path = filedialog.askopenfilename()
        selected_file["path"] = path
        label.config(text=f"Selected: {path}")

    # 🔐 Encrypt
    def encrypt_file():
        if not selected_file["path"]:
            label.config(text="No file selected!")
            return

        data = read_file(selected_file["path"])
        file_hash = get_hash(data).encode()

        encrypted = hybrid_encrypt(public_key, data + b"||" + file_hash)
        write_file(selected_file["path"] + ".enc", encrypted)

        label.config(text="✅ Encrypted Successfully")

    # 🔓 Decrypt
    def decrypt_file():
        if not selected_file["path"]:
            label.config(text="No file selected!")
            return

        data = read_file(selected_file["path"])
        decrypted = hybrid_decrypt(private_key, data)

        file_data, old_hash = decrypted.split(b"||")
        new_hash = get_hash(file_data).encode()

        if new_hash == old_hash:
            write_file("decrypted_" + selected_file["path"].split("/")[-1], file_data)
            label.config(text="✅ Decrypted (File Safe)")
        else:
            label.config(text="❌ File Modified!")

    # ☁️ Upload
    def upload_to_cloud():
        if selected_file["path"]:
            msg = upload_file(selected_file["path"])
            label.config(text=msg)
        else:
            label.config(text="Select file first!")

    # ☁️ Download
    def download_from_cloud():
        if not selected_file["path"]:
            label.config(text="Select file first!")
            return

        filename = selected_file["path"].split("/")[-1]
        msg = download_file(filename, "downloaded_" + filename)
        label.config(text=msg)

    # 🔑 Export Keys
    def export_keys():
        save_private_key(private_key)
        save_public_key(public_key)
        label.config(text="🔑 Keys Exported")

    # 🔑 Import Keys
    def import_keys():
        global private_key, public_key
        private_key = load_private_key()
        public_key = load_public_key()
        label.config(text="🔑 Keys Imported")

    # UI Elements
    drop_area = tk.Label(app, text="Drag & Drop File Here", bg="lightgray", width=40, height=5)
    drop_area.pack(pady=10)

    drop_area.drop_target_register(DND_FILES)
    drop_area.dnd_bind('<<Drop>>', drop)

    tk.Button(app, text="Browse File", command=browse_file).pack(pady=5)
    tk.Button(app, text="Encrypt", command=encrypt_file).pack(pady=5)
    tk.Button(app, text="Decrypt", command=decrypt_file).pack(pady=5)

    # 🔥 NEW BUTTONS
    tk.Button(app, text="Upload to Cloud", command=upload_to_cloud).pack(pady=5)
    tk.Button(app, text="Download from Cloud", command=download_from_cloud).pack(pady=5)

    tk.Button(app, text="Export Keys", command=export_keys).pack(pady=5)
    tk.Button(app, text="Import Keys", command=import_keys).pack(pady=5)

    label = tk.Label(app, text="")
    label.pack(pady=10)

    app.mainloop()