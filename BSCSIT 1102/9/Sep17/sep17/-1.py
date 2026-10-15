"""
Grade Filter Program
Purpose: Display students with grades above a user specified threshold.
"""

def filter_grades():
    grades_dict = {
        "Dwein": 80,
        "Seagal": 85,
        "Arnold": 90,
        "Statham": 60,
        "Randy": 65
    }

    try:
        threshold = float(input("Enter the minimum grade threshold: "))
        print(f"\nStudents with grades >= {threshold}:")
        found = False
        for name, grade in grades_dict.items():
            if grade >= threshold:
                print(name)
                found = True
        if not found:
            print(f"No students have grades >= {threshold}")
    except ValueError:
        print("Please enter a valid number!")

# Entry point
if __name__ == "__main__":
    filter_grades()