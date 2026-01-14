import pandas as pd
import os

print(">>> Executing File Renamer with Mapping File.\n")

# Find and read the mapping .csv file
curr_dir = os.getcwd()
csv_mapping_file = "rename-map"
target_folder = "raw files"

for root, dirs, files in os.walk(curr_dir):
    for i in files:
        if csv_mapping_file in i:
            inputFileDir = os.path.join(root, i)
            data1 = pd.read_csv(os.path.join(root, i))

# Get required information from .csv file
newNameList = data1["Title"]
extensionList = data1["FileExtension"]

# Rename the files
for root, dirs, files in os.walk(os.getcwd() + "/" + target_folder):
    for fileName in files:
        index = data1[data1["Id"] == fileName].index.values[0]
        newFileName = newNameList[index] + "." + extensionList[index]

        os.rename( os.path.join(root, fileName), os.path.join(root, newFileName) )

print("--- END ---")