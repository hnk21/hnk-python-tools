# hnk-python-tools
Personal repository of productivity related scripts made using Python.

At the current state, all of the scripts are developed separately within their own folders, for ease of maintenance and personally for more modular use cases. 

Last updated: 2026-03-22

## excel-tools
### 01_get_info.py
- Looks into a user-defined target folder, and gets the number of columns and rows for each Excel file (.xlsx / .csv).
- The result is saved into a .txt file.

### 02_record_finder.py
- Assumes the Excel file to be a database table.
- Function 1: Find a specific row.
- Function 2: For a specific column, identify rows with values under that column that exceed a defined character length.

### 03_split_csv.py
- Primarily used on very large .csv files.
- Splits a .csv file into multiple .csv files, depending on the user-defined maximum number of rows per .csv file.
    - For example, lets say we want to split a .csv file of 321,000 rows into portions of at most 100,000 rows each.
    - The script will produce 3 files of 100,000 rows each and 1 file of 21,000 rows.
 
### 04_combine_excel.py
- Combines Excel files (.xlsx / .csv) into one .xlsx file.
- With choice of:
    1. Each file is combined as one sheet
    2. All files combined into one sheet

### 12_compare_excel.py
- Compares two selected Excel files (.xlsx / .csv) to check if they have the same number of rows/columns.

### 13_data_entry_tool.py
- A simple datatable entry tool, will develop this into something bigger if I happen to find a cool and useful use case.

---

## file-tools
### 01_get_file_names.py
- Gets all file names from a target folder.

### 02_delete_old_files.py
- Deletes files from a target folder with a last modified date that is more than x days old.

### 03_rename.py
- Simple script for renaming files by replacing a specified string with another.

### 04_rename_with_file.py
- File renamer script that uses an input file.
- Input file is a mapping file that contains two columns: curr_file_name, new_file_name