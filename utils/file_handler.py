import os

def validate_file(path):
    return os.path.exists(path) and os.path.isfile(path)
