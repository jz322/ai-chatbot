from functions.write_file import write_file

def main():
    command = "python.py"

    if command.endswith('py') == True:
        print("this works")
    else:
        print("This does not work")
if __name__ == "__main__":
    main()