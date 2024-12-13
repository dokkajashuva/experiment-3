# Dictionary of employees
employees = {
    "John Doe": {"age": 28, "salary": 55000},
    "Jane Smith": {"age": 35, "salary": 60000},
    "Emily Johnson": {"age": 42, "salary": 72000},
    "Michael Brown": {"age": 30, "salary": 48000},
    "Linda Davis": {"age": 25, "salary": 51000}
}

# Printing the employee data
for name, details in employees.items():
    print(f"Employee Name: {name}")
    print(f"Age: {details['age']}")
    print(f"Salary: ${details['salary']}")
    print("----")
