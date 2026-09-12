import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

# Email config (use your credentials)
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
