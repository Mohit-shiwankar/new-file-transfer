import os
from flask import send_file, jsonify
from utils.file_utils import secure_filename_custom
from services.email_service import send_email_notification
from config import UPLOAD_FOLDER

def save_file(file):
    filename = secure_filename_custom(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(file_path)

    # send email after upload
    send_email_notification(filename)

    return file_path


def get_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(file_path, as_attachment=True)
