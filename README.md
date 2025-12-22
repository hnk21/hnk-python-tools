# hnk-python-tools
Personal repository of Python scripts developed for productivity related tasks
Actively updating this as of 2025-12-22

## excel-tools
excel_01_get_info.py
    - Looks into a user-defined target folder, and gets the number of columns and rows for each .xlsx or .csv file.
    - The result is saved into a .txt file.

excel_02_record_finder.py
    - Assumes the Excel file to be a database table.
    - Function 1: Find a specific row.
    - Function 2: For a specific column, identify rows with values under that column that exceed a defined character length.

excel_03_split_csv.py
    - Primarily used on very large .csv files.
    - Splits a .csv file into multiple .csv files, depending on the user-defined maximum number of rows per .csv file.
        - e.g. I wish to split a .csv file of 321,000 rows into multiple .csv files with at most 100,000 rows each.
        
        The script will produce 4 .csv files (3 files of 100,000 rows each and 1 file of 21,000 rows)


## file-tools