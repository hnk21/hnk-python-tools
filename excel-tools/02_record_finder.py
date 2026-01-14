import pandas as pd
import os

curr_dir = os.getcwd()
folder_to_search = "files_to_search"

# 1 - Find specific record in Excel file ###
def findRecords(column_to_search_1, target_value_1, column_to_search_2, target_value_2):
    for root, dirs, files in os.walk(curr_dir):
        if folder_to_search in root:
            for f in files:
                if ".xlsx" in f:
                    input_data = pd.read_excel(root + "\\" + f, dtype = {column_to_search_1: "string", column_to_search_2: "string"})
                elif ".csv" in f:
                    input_data = pd.read_csv(root + "\\" + f, dtype = {column_to_search_1: "string", column_to_search_2: "string"})

                if input_data is not None:
                    print(f"Searching file {f}...")
                    column1 = input_data[column_to_search_1].tolist()
                    column2 = input_data[column_to_search_2].tolist()

                    if any( [(value1 in target_value_1 for value1 in column1), (value2 in target_value_2 for value2 in column2)] ):
                        for i in range(0, len(column1)):
                            if column1[i] in target_value_1:
                                print(f"Target value {column1[i]} found on {column_to_search_1} > row {i+2}")

                            elif column2[i] in target_value_2:
                                print(f"Target value {column2[i]} found on {column_to_search_1} > row {i+2}")

# 2 - For a specific column, identify values that exceed a defined character length
def getLengthOfColumnValues(column_name, targetLength):
    for root, dirs, files in os.walk(curr_dir):
        if folder_to_search in root:
            for f in files:
                if ".xlsx" in f:
                    input_data = pd.read_excel(root + "\\" + f, dtype = {column_to_search_1: "string", column_to_search_2: "string"})
                elif ".csv" in f:
                    input_data = pd.read_csv(root + "\\" + f, dtype = {column_to_search_1: "string", column_to_search_2: "string"})

                print(f"Searching file {f}...")
                column1 = input_data[column_name].tolist()

                for i in range(0, len(column1)):
                    if len(column1[i]) > targetLength:
                        print(f"Row {i+2} > value '{column1[i]}' exceeds {targetLength} characters")

# User defined variables
# 1 - Specify the columns to search from and the values to search for 
column_to_search_1 = "Item Number"
target_value_1 = ["1584C002AA"]

column_to_search_2 = "Country code"
target_value_2 = ["1584C002AA"]

print(f"Finding rows under column {column_to_search_1} with target value {target_value_1} OR under column {column_to_search_2} with target value {target_value_2}.")
findRecords(column_to_search_1, target_value_1, column_to_search_2, target_value_2)

# 2 - Specify the column name and the target character length
column_name = "Item Name"
target_length = 80

print(f"Running function to get length of values of specific column {column_name} that exceed {target_length} characters.")
getLengthOfColumnValues(column_name, target_length)

print("--- END ---")