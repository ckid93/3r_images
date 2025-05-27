import os
import subprocess

# Run the Git command to list files
result = subprocess.run(["git", "ls-tree", "-r", "main", "--name-only"], capture_output=True, text=True)
files = result.stdout.splitlines()

# Filter for files in the 'image_p1' folder
image_p1_files = [f for f in files if "image_p1/" in f]

# Print the count
print(f"Number of files in image_p1: {len(image_p1_files)}")
