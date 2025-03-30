students = [
    {
        "first_name": "Buse",
        "last_name": "Nazla",
        "index_number": "34373",
        "nationality": "turkısh",
        "starting_date": "2025-03-30",
        "courses": ["Mathematics", "Physics", "Computer Science"]
    },
    {
        "first_name": "Alice",
        "last_name": "Smith",
        "index_number": "S67890",
        "nationality": "British",
        "starting_date": "2024-09-01",
        "courses": ["Biology", "Chemistry", "English"]
    },
    {
        "first_name": "Michael",
        "last_name": "Johnson",
        "index_number": "S54321",
        "nationality": "Canadian",
        "starting_date": "2023-06-15",
        "courses": ["History", "Geography", "Philosophy"]
    }
]

for student in students:
    print(f"Name: {student['first_name']} {student['last_name']}, Index: {student['index_number']}")
