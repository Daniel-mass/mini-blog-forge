import os

def print_tree(start_path, prefix=""):
    # Get all files and folders in the directory
    files = os.listdir(start_path)
    files.sort()

    for index, file in enumerate(files):
        path = os.path.join(start_path, file)
        connector = "├── " if index < len(files) - 1 else "└── "
        print(prefix + connector + file)

        if os.path.isdir(path):
            extension = "│   " if index < len(files) - 1 else "    "
            print_tree(path, prefix + extension)

if __name__ == "__main__":
    print("📂 Project Structure:\n")
    print_tree(".")
