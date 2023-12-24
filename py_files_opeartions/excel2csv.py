import pandas as pd

read_file = pd.read_excel(
    "D:\\WorkDesk\\Python\\py_Fundamentals\\py_Fundamentals\\file\\excel.xlsx", sheet_name='Data Mapping')

print("Columns: Before Modification: ", read_file.columns)

for ind in range(len(read_file.columns)):
    read_file.columns.values[ind] = read_file.columns.values[ind].replace(
        '\n', ' ')
    read_file.columns.values[ind] = ' '.join(
        read_file.columns.values[ind].split())

print("Columns: After new line replacement Modification: ", read_file.columns)

new_data = read_file[["Col 1", "Col 2", "Col 3"]]
new_data.to_csv(
    "D:\\WorkDesk\\Python\\py_Fundamentals\\py_Fundamentals\\file\\excel.csv", index=None, header=True)
