import os


def change_file_extension(folder_path, old_extension, new_extension):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_extension):
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(
                folder_path, filename.rsplit(
                    old_extension, 1)[0] + new_extension)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")
