from functions.write_file import write_file

def main():
    # 1. lorem.txt (to check truncation)
    first = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(first)

    # 2. main.py
    second = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(second)

    # 3. pkg/calculator.py
    third = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(third)

if __name__ == "__main__":
    main()