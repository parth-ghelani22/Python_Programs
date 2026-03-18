import pandas as pd

# Update this path to include your specific file name
file_path = r"D:\4053\Python\Unit 4"

#For load file path
df = pd.read_excel("Student Data.xlsx")

print("Columns in the file:")
print(df.columns.tolist())

# Display data types
print("\nData types of each column:")
print(df.dtypes)
