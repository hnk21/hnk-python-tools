import os
import csv
from tkinter.filedialog import askopenfilename

row_limit = 100000 # Define the number of rows per split file

def split_csv(input_file, row_limit, output_prefix):
    with open(input_file, 'r', newline = '', encoding = "utf8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        
        file_number = 1
        rows_written = 0
        
        output_file = f"{output_prefix}_{file_number}.csv"
        outfile = open(output_file, 'w', newline = '', encoding = "utf8")
        writer = csv.writer(outfile)
        writer.writerow(header)
        
        for row in reader:
            if rows_written >= row_limit:
                outfile.close()
                file_number += 1
                rows_written = 0
                output_file = f"{output_prefix}_{file_number}.csv"
                outfile = open(output_file, 'w', newline = '', encoding = "utf8")
                writer = csv.writer(outfile)
                writer.writerow(header)
                
            writer.writerow(row)
            rows_written += 1
        
        outfile.close()

        return file_number

filename = ""

while ".csv" not in filename:
    print(">>> Please select the .csv file to be split.")
    filepath = askopenfilename()
    filename = os.path.basename(filepath)
    print(f">>> Selected file: {filename}")

with open(filepath, 'r', newline='', encoding="utf8") as csvfile:
    rows = sum(1 for row in csv.reader(csvfile))

print(f">>> Selected file has {rows} rows.")
print(f">>> Processing {filename} now...")
output_filename = filename.replace(".csv", "")
num_of_files = split_csv(filepath, row_limit, output_filename)

print(f"Finished spltting {filename} into {num_of_files} parts, with maximum of {row_limit} rows each.")
print("--- END ---")