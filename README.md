# hnk-python-tools
Personal repository of productivity related scripts made using Python.

At the current state, all of the scripts are developed separately within their own folders, for ease of maintenance and personally for more modular use cases. 

Latest significant commit: 2026-01-11

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
- Combines all Excel files (.xlsx / .csv) into one file.

### 12_compare_excel.py
- Compares two selected Excel files (.xlsx / .csv) to check if they have the same number of rows/columns.
- Not committed to this repository yet.

### 13_data_entry_tool.py
- A simple datatable entry tool, will develop this into something bigger if I happen to find a cool and useful use case.
- Not committed to this repository yet.

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
- Not committed to this repository yet

---

## web-tools
### mal_scraper
- Website scraper that extracts anime data from [myanimelist.com](https://myanimelist.net/)
- Features
    - Currently reads from an input .csv file that contains a table of anime data.
    - Each row has a link to the corresponding mal entry.
    - The code extracts a few details from each link, then updates the input .csv file.
- Not committed to this repository yet.

### cna_scraper
- Website scraper that extracts news article links from [https://www.channelnewsasia.com/](https://www.channelnewsasia.com/)
- Filters for news articles ofthe following categories:
    - Business, Singapore, Asia, East Asia, World, Sustainability, Commentary
- Not committed to this repository yet.
