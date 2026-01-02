import os
from google import genai
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    
    abs_path = os.path.abspath(working_directory)
   
    target_dir = os.path.normpath(os.path.join(abs_path, directory))
   
    valid_target_dir = os.path.commonpath([abs_path, target_dir]) == abs_path

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{target_dir}" is not a directory'

        

    string = []
    file_list = os.listdir(target_dir)
    try:
        for file in file_list:
            file_abs = os.path.join(target_dir, file)
            string.append(f"- {file}: file_size={os.path.getsize(file_abs)} bytes, is_dir={os.path.isdir(file_abs)}")
        new_string = "\n".join(string)
        return new_string

    except:
        return "Error: unknown file type"

    




