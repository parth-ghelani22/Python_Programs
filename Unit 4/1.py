import pandas as pd
#loads file path
file_path = r"D:\4053\Python\Unit 4"

#load file
df = pd.read_excel("Student Data.xlsx")

print("Columns in the file:")
print(df.columns.tolist())

print("\nData types of each column:")
print(df.dtypes)
