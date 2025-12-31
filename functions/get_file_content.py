import os
from config import CHAR_LIMIT

def get_file_content(working_directory, file_path):

    abs_path_working_directory = os.path.abspath(working_directory)
    
    target_dir = os.path.normpath(os.path.join(abs_path_working_directory, file_path))

    valid_target_dir = os.path.commonpath([abs_path_working_directory, target_dir]) == abs_path_working_directory

    if valid_target_dir == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(target_dir) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'

    file = open(target_dir)

    file_text = file.read(CHAR_LIMIT)
    extra = file.read(1)
    
    if extra != "":
        file_text += f'\n[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'

    return file_text
