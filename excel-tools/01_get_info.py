import os
import pandas as pd
from datetime import datetime

def getExcelInfo(folderToSearch):
    curr_dir = os.getcwd()

    # Find the folder to be searched
    for root, dirs, files in os.walk(curr_dir):
        if folderToSearch in root:
            os.chdir(root)
            os.chdir('..')

            # Create a .txt file to save the file information
            logfile = open(folderToSearch + "_excel_info" + ".txt", "a", encoding = 'utf8')
            logfile.write("Log updated as of {} \n".format(datetime.now().strftime("%G%m%d_%H%M")))

            print(f"Analysing files from folder >>> [{root}]")

            for f in files:
                if ".csv" in f:
                    df = pd.read_csv(root + "/" + f)
                elif ".xlsx" in f:
                    df = pd.read_excel(root + "/" + f)

                if df is not None:
                    print(f"Reading file >>> [{f}]")

                    col_count, row_count = len(df.axes[1]), len(df.axes[0])

                    col_log = f"Column Count: {col_count}"
                    row_log = f"Row Count: {row_count}"
                    print(col_log + "\n" + row_log + "\n")
                    logfile.write(f + "\n" + col_log + "\n" + row_log + "\n\n")

            logfile.close()


folderToSearch = "files_to_search" # Define the folder that contains Excel files to analyse

getExcelInfo(folderToSearch)

print("--- END ---")