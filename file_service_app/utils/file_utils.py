import re

def secure_filename_custom(filename):
    filename = filename.strip().replace(" ", "_")
    filename = re.sub(r"[^a-zA-Z0-9_.-]", "", filename)
    return filename
