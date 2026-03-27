""" 2. Write a program to load above excel file and display following information
- List of students from Rajkot City
- List of Male students
- List of Male students from Rajkot City
- List of students whose age >= 20 """
import pandas as pd

file_path = r"D:\4053\Python\Unit 4"
df = pd.read_excel("Student Data.xlsx")

print("\nStudents from Rajkot:")
print(df[df["City"] == "Rajkot"])

print("\nMale Students:")
print(df[df["Gender"] == "Male"])

print("\nMale Students from Rajkot:")
print(df[(df["Gender"] == "Male") & (df["City"] == "Rajkot")])

print("\nStudents Age >= 20:")
print(df[df["Age"] >= 20])
