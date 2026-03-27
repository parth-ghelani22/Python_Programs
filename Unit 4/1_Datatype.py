"""  Create an excel file with columns RollNo, Name, Gender, E-Mail, Mobile, Age and City. Enter atleast 20 records and then perform following exercise
1) Write a program to load above excel file and display columns of file and data type of each column """

import pandas as pd
#loads file path
file_path = r"D:\4053\Python\Unit 4"

#load file
df = pd.read_excel("Student Data.xlsx")

print("Columns in the file:")
print(df.columns.tolist())

print("\nData types of each column:")
print(df.dtypes)
