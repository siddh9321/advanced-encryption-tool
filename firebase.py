import firebase_admin
from firebase_admin import credentials, storage
import os

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-project-id.appspot.com'
})

bucket = storage.bucket()

def upload_file(local_path):
    blob = bucket.blob(os.path.basename(local_path))
    blob.upload_from_filename(local_path)
    return f"Uploaded: {blob.name}"

def download_file(filename, destination):
    blob = bucket.blob(filename)
    blob.download_to_filename(destination)
    return f"Downloaded: {destination}"