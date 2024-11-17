import os
import shutil
import re

# Directories (modify these if necessary)
source_dir = "data"  # Directory where all files are currently located
beginners_dir = "data 8x8"
intermediate_dir = "data 16x16"
expert_dir = "data 16x30"

# Make sure the destination directories exist
os.makedirs(beginners_dir, exist_ok=True)
os.makedirs(intermediate_dir, exist_ok=True)
os.makedirs(expert_dir, exist_ok=True)

# Regular expressions to match the filenames
beginner_pattern = r'^beginner(\d+)\.txt$'
intermediate_pattern = r'^intermediate(\d+)\.txt$'
expert_pattern = r'^expert(\d+)\.txt$'

# Get the list of files in the source directory
files = os.listdir(source_dir)

# Loop through each file and copy it to the corresponding directory
for file in files:
    file_path = os.path.join(source_dir, file)

    # Skip directories (in case there are any directories mixed in)
    if os.path.isdir(file_path):
        continue

    # Check if the file matches the beginner pattern
    if re.match(beginner_pattern, file):
        dest_path = os.path.join(beginners_dir, file)
        try:
            shutil.copy(file_path, dest_path)
            print(f"Copied {file} to {beginners_dir}")
        except Exception as e:
            print(f"Failed to copy {file} to {beginners_dir}: {e}")

    # Check if the file matches the intermediate pattern
    elif re.match(intermediate_pattern, file):
        dest_path = os.path.join(intermediate_dir, file)
        try:
            shutil.copy(file_path, dest_path)
            print(f"Copied {file} to {intermediate_dir}")
        except Exception as e:
            print(f"Failed to copy {file} to {intermediate_dir}: {e}")

    # Check if the file matches the expert pattern
    elif re.match(expert_pattern, file):
        dest_path = os.path.join(expert_dir, file)
        try:
            shutil.copy(file_path, dest_path)
            print(f"Copied {file} to {expert_dir}")
        except Exception as e:
            print(f"Failed to copy {file} to {expert_dir}: {e}")
