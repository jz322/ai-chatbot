import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_path_working_directory = os.path.abspath(working_directory)
    
    target_dir = os.path.normpath(os.path.join(abs_path_working_directory, file_path))
    
    valid_target_dir = os.path.commonpath([abs_path_working_directory, target_dir]) == abs_path_working_directory

    if valid_target_dir == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(target_dir) == False:
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if target_dir.endswith('py') == False:
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_dir]

    if args:
        command.extend(args)

    
    result = subprocess.run(command, cwd=abs_path_working_directory, capture_output=True, text=True, timeout=30)
    
    output = ""
    
    if result.returncode != 0:
        output += f"Process exited with code {result.returncode}\n"

    if not result.stdout and not result.stderr:
        output += "No output produced"

    if result.stdout:
        output += f"STDOUT:\n{result.stdout}"

    if result.stderr:
        output += f"STDERR:\n{result.stderr}"

    return output
