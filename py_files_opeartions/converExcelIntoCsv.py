# importing pandas as pd
import pandas as pd

import os
# <-- absolute dir the script is in
# script_dir = os.chdir(
#     "D\WorkDesk\Python\py_Fundamentals\py_Fundamentals\file\Test.xlsx")
# print(script_dir)
# excelRel_path = "file\\Test.xlsx"
# csvRel_path = "file\\Test.csv"


# abs_file_pathExcel = os.chdir(
#     "D\WorkDesk\Python\py_Fundamentals\py_Fundamentals\file\Test.xlsx")

# abs_file_pathCsv = os.chdir(
#     "D\WorkDesk\Python\py_Fundamentals\py_Fundamentals\file\Test.csv")

# Read and store content
# of an excel file
read_file = pd.read_excel(
    "D:\\WorkDesk\\Python\\py_Fundamentals\\py_Fundamentals\\file\\Test.xlsx")

# Write the dataframe object
# into csv file
read_file.to_csv("D:\\WorkDesk\\Python\\py_Fundamentals\\py_Fundamentals\\file\\Test.csv",
                 index=None,
                 header=True)

# read csv file and convert
# into a dataframe object
df = pd.DataFrame(pd.read_csv(
    "D:\\WorkDesk\\Python\\py_Fundamentals\\py_Fundamentals\\file\\Test.csv"))

# show the dataframe
df
