import os


def rename_files_in_folder(folder_path, prefix):
    try:
        # List all files in the directory
        files = [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        files.sort()  # Sorting to ensure a consistent order

        # Rename each file
        for i, filename in enumerate(files):
            file_extension = os.path.splitext(filename)[1]
            new_name = f"{prefix}{i+1}{file_extension}"
            os.rename(
                os.path.join(folder_path, filename), os.path.join(folder_path, new_name)
            )

        print("Renaming completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage
folder_path = "C:\\Users\\micha\\Desktop\\chdcho\\fotky\\darkove"
prefix = "darkove"
rename_files_in_folder(folder_path, prefix)
