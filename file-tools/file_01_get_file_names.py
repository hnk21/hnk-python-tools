import os
from tkinter import filedialog

print(">>> Executing script to get file names.\n")

print("> Please select the target folder.")

folder_to_search = filedialog.askdirectory(title = "Select Folder")
print(f"> Selected folder: {folder_to_search}\n")
log_file = folder_to_search + "_file_names.txt"

# Find the folder to be searched
for root, dirs, files in os.walk(folder_to_search):
    if folder_to_search in root:
        os.chdir(root)
        os.chdir('..')

        # Create a .txt file to log all the file names in
        logfile = open(log_file, "a", encoding = 'utf8')

        print(f"> Getting all file names from folder [{root}]...\n")
        for f in files:
            logfile.write(f + "\n")
        print("> done\n")
        
        break

print(f">>> File names in folder [{folder_to_search}] are logged in [{log_file}]\n")
logfile.close()

print("--- END ---")