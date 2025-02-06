import pandas as pd
import os

FILE_NAME = "employees.xlsx"

def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_excel(FILE_NAME)
    else:
        return pd.DataFrame(columns=["Employee ID", "Name", "Age", "Department", "Salary"])

def save_data(df):
    df.to_excel(FILE_NAME, index=False)

def generate_employee_id(df):
    return 1001 if df.empty else df["Employee ID"].max() + 1

def add_employee():
    df = load_data()
    emp_id = generate_employee_id(df)
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    new_employee = pd.DataFrame([[emp_id, name, age, department, salary]], columns=df.columns)
    df = pd.concat([df, new_employee], ignore_index=True)
    save_data(df)
    print(f"Employee {name} added successfully with Employee ID: {emp_id}")

def view_employees():
    df = load_data()
    print(df if not df.empty else "No employee records found.")

def search_employee():
    df = load_data()
    if df.empty:
        print("No employee records found.")
        return
    
    criteria = input("Search by (id/name/salary): ").strip().lower()
    
    if criteria == "id":
        emp_id = int(input("Enter Employee ID: "))
        result = df[df["Employee ID"] == emp_id]
    elif criteria == "name":
        name = input("Enter Name: ").strip()
        result = df[df["Name"].str.contains(name, case=False, na=False)]
    elif criteria == "salary":
        salary = float(input("Enter Salary: "))
        result = df[df["Salary"] == salary]
    else:
        print("Invalid criteria.")
        return
    
    print(result if not result.empty else "No matching records found.")

def update_employee():
    df = load_data()
    emp_id = int(input("Enter Employee ID to update: "))
    index = df[df["Employee ID"] == emp_id].index
    
    if index.empty:
        print("Employee not found.")
        return
    
    name = input("Enter new Name (leave blank to keep unchanged): ").strip()
    age = input("Enter new Age (leave blank to keep unchanged): ").strip()
    department = input("Enter new Department (leave blank to keep unchanged): ").strip()
    salary = input("Enter new Salary (leave blank to keep unchanged): ").strip()
    
    if name:
        df.at[index[0], "Name"] = name
    if age:
        df.at[index[0], "Age"] = int(age)
    if department:
        df.at[index[0], "Department"] = department
    if salary:
        df.at[index[0], "Salary"] = float(salary)
    
    save_data(df)
    print("Employee updated successfully.")

def delete_employee():
    df = load_data()
    emp_id = int(input("Enter Employee ID to delete: "))
    df = df[df["Employee ID"] != emp_id]
    save_data(df)
    print("Employee deleted successfully.")
