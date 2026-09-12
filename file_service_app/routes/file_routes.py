from flask import Blueprint, request, jsonify
from services.file_service import save_file, get_file

file_bp = Blueprint("file_bp", __name__)

@file_bp.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    file_path = save_file(file)
    return jsonify({"message": "File uploaded", "path": file_path})


@file_bp.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return get_file(filename)
