import os

print(">>> Executing Basic File Renamer.\n")

# Set the target directory containing the files to rename
curr_dir = os.getcwd()
print(f"Current directory: '{curr_dir}'")
target_dir = curr_dir + '/file-tools/target_folder/'
print(f"Target directory: '{target_dir}'")

# Set the prefix
old = "apple"
new = "orange"

def rename(target_dir, old_string, new_string):
    for filename in os.listdir(target_dir):
        if old_string in filename:
            new_filename = filename.replace(old_string, new_string)
            os.rename(os.path.join(target_dir, filename), os.path.join(target_dir, new_filename))
            print(f"Renamed '{filename}' to '{new_filename}'")

rename(target_dir, old, new)

print("--- END ---")