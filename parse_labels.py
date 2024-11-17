import os

board_sizes = ["8x8", "16x16", "16x30"]
for board_size in board_sizes:
    labels_dir = f"labels {board_size}"
    data_dir = f"data {board_size}"

    labels_files = set(os.listdir(labels_dir))
    data_files = set(os.listdir(data_dir))

    files_to_delete = labels_files - data_files

    for file in files_to_delete:
        file_path = os.path.join(labels_dir, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
