import os

UPLOAD_FOLDER = "uploads"

def get_file_path(filename: str):
    return os.path.join(UPLOAD_FOLDER, filename)


def read_file_content(filepath: str):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except Exception:
        return None
