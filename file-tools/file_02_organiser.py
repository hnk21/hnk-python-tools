import aiofiles.os
import asyncio
import os
import time
from tkinter import filedialog

print(">>> Executing script to delete old files.\n")

print("> Please select the target folder.")

folder_empty = True
while folder_empty:
    folder_to_search = filedialog.askdirectory(title = "Select Folder")
    print(f"> Selected folder: {folder_to_search}\n")

    folder_empty = len(os.listdir(folder_to_search)) == 0
    if folder_empty:
        print("> Selected folder is empty, please select a folder that contains files.")

print("> Please enter a whole number, which represents the threshold for the number of days.")
print("> Note that files that were last modified for more than this number of days old will be deleted.\n")

input_check = True
while input_check == True:
    number_of_days = input("> Number of days: ")
    try:
        number_of_days = int(number_of_days)
        input_check = False
    except:
        print("> Input must be a number, please try again.\n")

print(f"> Number of days entered: {number_of_days}\n")
print(f"> Deleting files that are more than {number_of_days} days old from [{folder_to_search}]...")

async def clean_up(folder_path, number_of_days):
    now = time.time()
    cutoff_time = now - (number_of_days * 86400)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.getmtime(file_path) < cutoff_time:
            await aiofiles.os.remove(file_path)
            print(f"> Deleted [{filename}]")
    
    print("> done\n")

asyncio.run(clean_up(folder_to_search, number_of_days))

print("--- END ---")