import os

board_sizes = ["8x8", "16x16", "16x30"]
board_mines = {"8x8": 10, "16x16": 40, "16x30": 99}
for board_size in board_sizes:
    data_dir = f"data {board_size}"


    # Function to check if a board is "solved"
    def is_solved(file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                # Check for exactly 10 'F' characters and no '-' characters
                return content.count('F') == board_mines[board_size] and '-' not in content
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return False


    # Get the list of filenames in the 'data 8x8' directory
    data_files = os.listdir(data_dir)

    # Loop through the files and delete the solved ones
    for file in data_files:
        file_path = os.path.join(data_dir, file)

        if is_solved(file_path):
            try:
                os.remove(file_path)  # Delete the file
                print(f"Deleted from data 8x8: {file_path}")
            except Exception as e:
                print(f"Failed to delete from data 8x8: {file_path}: {e}")
