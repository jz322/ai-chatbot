from functions.get_file_content import get_file_content

def main():
    # 1. lorem.txt (to check truncation)
    lorem = get_file_content("calculator", "lorem.txt")
    print(lorem)

    # 2. main.py
    main_py = get_file_content("calculator", "main.py")
    print(main_py)

    # 3. pkg/calculator.py
    calc_py = get_file_content("calculator", "pkg/calculator.py")
    print(calc_py)

    # 4. /bin/cat (should be an error)
    bin_cat = get_file_content("calculator", "/bin/cat")
    print(bin_cat)

    # 5. non-existent file (should be an error)
    missing = get_file_content("calculator", "pkg/does_not_exist.py")
    print(missing)

if __name__ == "__main__":
    main()