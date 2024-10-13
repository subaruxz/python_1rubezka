students = [
    {"name": "Alice", "age": 21},
    {"name": "Charlie", "age": 23}
]

for student in students:
    for key, value in student.items():
        print(f"{key}: {value}")
    print()