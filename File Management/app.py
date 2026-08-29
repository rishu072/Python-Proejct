import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully.")
    except FileExistsError:
        print(f"File '{filename}' already exists.")
    except Exception as E:
        print(f"An error occurred: {E}")

def view_all_files():
        files = os.listdir('.')
        if not files:
            print("No files found in the current directory.")
        else:
            print("Files in the current directory:")
            for file in files:
                print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as E:
        print(f"An error occurred: {E}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as E:
        print(f"An error occurred: {E}")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            new_content = input("Enter the content to append: ")
            f.write(new_content + '\n')
            print(f"Content appended to '{filename}' successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as E:
        print(f"An error occurred: {E}")

def main():

    while True:

        print("\nFile Management Menu:")
        print("1. Create File")
        print("2. View All Files")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            filename = input("Enter the filename to create: ")
            create_file(filename)

        elif choice == '2':

            view_all_files()

        elif choice == '3':

            filename = input("Enter the filename to delete: ")
            delete_file(filename)

        elif choice == '4':

            filename = input("Enter the filename to read: ")
            read_file(filename)

        elif choice == '5':

            filename = input("Enter the filename to edit: ")
            edit_file(filename)

        elif choice == '6':

            print("Exiting...")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()