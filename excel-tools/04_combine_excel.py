import os
import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog

curr_dir = os.getcwd()
# print(f"Current directory: {curr_dir}\n")

# Select directory
def setup():
    print("Select the folder directory containing the Excel files you wish to combine.")
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title='Select Folder Directory')

    # Find .xlsx / .csv files
    if folder_path:
        xlsx_files = glob.glob(os.path.join(folder_path, '*.xlsx'))
        csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

        print(f"Selected the target folder '{folder_path}', which contains:")

        if not xlsx_files and not csv_files:
            print("> No .xlsx or .csv files\n")
        else:
            print(f"> {len(xlsx_files)} .xlsx files")
            print(f"> {len(csv_files)} .csv files\n")

            excel_files = xlsx_files + csv_files
            user_input(excel_files)
    else:
        print("No folder directory was selected.\n")

# User Decisions
def user_input(excel_files):
    # print("Proceed to combine these files? (y/n)")
    # proceed = input(">>> ")

    print("Choose the type of combine.")
    print("> 1. Each file as a separate sheet.")
    print("> 2. All files combined into one sheet.")
    combine_type = str()
    
    while not combine_type:
        combine_type = input(">>> ")
        if combine_type not in ["1", "2"]:
            print("> The program did not understand which combine type to execute.")
            print("> Please enter either 1 or 2.\n")
            combine_type  = ""

    print("\nGive a name for the combined file. Do not specify the file extension.")
    file_name = input(">>> ") + ".xlsx"
    output_path = os.path.join(curr_dir, file_name)

    if combine_type == "1":
        combine_per_sheet(excel_files, output_path)
    elif combine_type == "2":
        combine_one_sheet(excel_files, output_path)

# 1 - Each file - One sheet
def combine_per_sheet(excel_files, output_path):
    with pd.ExcelWriter(output_path) as writer:
        for file in excel_files:
            sheet_name = os.path.basename(file).split('.')[0]
            
            sheet_name = sheet_name[:31] if len(sheet_name) > 31 else sheet_name

            if ".xlsx" in file:
                df = pd.read_excel(file)
            elif ".csv" in file:
                df = pd.read_csv(file)
            
            # Write the DataFrame to a specific sheet in the new Excel file
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"> Added {file} as sheet '{sheet_name}' to the combined file.")

    print(f"\n> Successfully combined the files into '{output_path}'\n")

# 2 - All files - One sheet
def combine_one_sheet(excel_files, output_path):
    df_list = []

    for file in excel_files:
        if ".xlsx" in file:
            df = pd.read_excel(file)
        elif ".csv" in file:
            df = pd.read_csv(file)

        df_list.append(df)
        print(f"> Added file '{file}' to the combined file.")

    merged_df = pd.concat(df_list, ignore_index=True)
    merged_df.to_excel(output_path, index=False)

    print(f"\n> Successfully combined the files into '{output_path}'\n")

setup()

print("--- END ---")