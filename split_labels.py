import os
import re

source_dir = "labels"
beginners_dir = "labels 8x8"
intermediate_dir = "labels 16x16"
expert_dir = "labels 16x30"

os.makedirs(beginners_dir, exist_ok=True)
os.makedirs(intermediate_dir, exist_ok=True)
os.makedirs(expert_dir, exist_ok=True)

beginner_pattern = r'^beginner(\d+)\.txt$'
intermediate_pattern = r'^intermediate(\d+)\.txt$'
expert_pattern = r'^expert(\d+)\.txt$'

def remove_first_two_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove the first two lines
        lines = lines[2:]

        return lines
    except Exception as e:
        print(f"Failed to read {file_path}: {e}")
        return None

def write_to_new_file(content, dest_path):
    try:
        with open(dest_path, 'w') as file:
            file.writelines(content)
        print(f"Written modified content to {dest_path}")
    except Exception as e:
        print(f"Failed to write to {dest_path}: {e}")

files = os.listdir(source_dir)

for file in files:
    file_path = os.path.join(source_dir, file)

    if os.path.isdir(file_path):
        continue

    modified_lines = remove_first_two_lines(file_path)

    if modified_lines is not None:
        if re.match(beginner_pattern, file):
            dest_path = os.path.join(beginners_dir, file)
            write_to_new_file(modified_lines, dest_path)

        elif re.match(intermediate_pattern, file):
            dest_path = os.path.join(intermediate_dir, file)
            write_to_new_file(modified_lines, dest_path)

        elif re.match(expert_pattern, file):
            dest_path = os.path.join(expert_dir, file)
            write_to_new_file(modified_lines, dest_path)
