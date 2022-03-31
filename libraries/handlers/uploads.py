import os
from pathlib import Path


def handle_uploaded_file(file, file_name):
    write_uploaded_file_to_dir(file, file_name, os.path.join(Path(__file__).resolve().parent.parent.parent
                                                             , 'media', 'uploads'))


def write_uploaded_file_to_dir(file, file_name, path_to_dir):
    with open(os.path.join(path_to_dir, file_name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

