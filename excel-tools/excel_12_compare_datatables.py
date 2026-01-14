import pandas as pd
import os
from tkinter.filedialog import askopenfilename

print(">>> Executing script that compares two .xlsx datatables.")

# Datatable 1
filename1 = ""
while ".xlsx" not in filename1:
    print(">>> Please select the first file.")
    filepath1 = askopenfilename()
    filename1 = os.path.basename(filepath1)
    print(">>> Selected file 1: ", filename1)

# Datatable 2
filename2 = ""
while ".xlsx" not in filename2:
    print(">>> Please select the second file.")
    filepath2 = askopenfilename()
    filename2 = os.path.basename(filepath2)
    print(">>> Selected file 2: ", filename2)

# Compare datatables
print(f">>> Comparing '{filename1}' and '{filename2}'...")
df1 = pd.read_excel(filepath1)
# print("> file 1's info")
# print(df1.shape)

df2 = pd.read_excel(filepath2)
# print("> file 2's info")
# print(df2.shape)

df1.compare(df2)
print("--- END ---")