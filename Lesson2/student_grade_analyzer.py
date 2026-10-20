"""Student Grade Analyzer - Version 2

Reads student records from grades.txt, validates data, classifies grades,
calculates statistics without built-in functions, allows searching, and saves a report.
"""


def classify_grade(grade):
    """Return the classification and status of a grade based on criteria."""
    if 90 <= grade <= 100:
        return "Excellent", "Passed"
    elif 85 <= grade < 90:
        return "Very Good", "Passed"
    elif 80 <= grade < 85:
        return "Good", "Passed"
    elif 75 <= grade < 80:
        return "Satisfactory", "Passed"
    elif 0 <= grade < 75:
        return "Needs Improvement", "Failed"
    else:
        return "Invalid", "Invalid"


def load_students(filename):
    """Read valid student records from a text file and return them as a list[cite: 2, 3]."""
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                cleaned = line.strip()
                # Skip blank lines and comment lines[cite: 1, 3]
                if not cleaned or cleaned.startswith("#"):
                    continue

                parts = cleaned.split(",")
                if len(parts) != 3:
                    continue

                student_id = parts[0].strip()
                name = parts[1].strip()

                try:
                    grade = float(parts[2].strip())
                except ValueError:
                    continue

                if 0 <= grade <= 100:
                    students.append({
                        "student_id": student_id,
                        "name": name,
                        "grade": grade
                    })
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError as error:
        print(f"Error reading file '{filename}': {error}")

    return students


def calculate_statistics(students):
    """Calculate and return class statistics without sum(), max(), or min()[cite: 2, 3]."""
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for s in students:
        g = s["grade"]
        total_grade += g

        _, status = classify_grade(g)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if g > highest_student["grade"]:
            highest_student = s
        if g < lowest_student["grade"]:
            lowest_student = s

    total_students = len(students)
    average = total_grade / total_students

    return {
        "total_students": total_students,
        "average": average,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }


def display_students(students):
    """Display all student records in a formatted table[cite: 2, 3]."""
    if not students:
        print("No student records available to display.")
        return

    print(f"\n{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<10}")
    print("-" * 70)
    for s in students:
        classification, status = classify_grade(s["grade"])
        print(f"{s['student_id']:<12} {s['name']:<20} {s['grade']:<8.2f} {classification:<18} {status:<10}")


def display_statistics(statistics):
    """Display the calculated class statistics[cite: 2, 3]."""
    if not statistics:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['total_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed_count']}")
    print(f"Failed: {statistics['failed_count']}")
    highest = statistics["highest_student"]
    lowest = statistics["lowest_student"]
    print(f"Highest: {highest['name']} - {highest['grade']:.2f}")
    print(f"Lowest: {lowest['name']} - {lowest['grade']:.2f}")


def search_student(students, keyword):
    """Return records whose student number or name matches the keyword[cite: 2, 3]."""
    matches = []
    clean_keyword = keyword.strip().lower()

    if not clean_keyword:
        return matches

    for s in students:
        s_id = s["student_id"].lower()
        s_name = s["name"].lower()
        if clean_keyword in s_id or clean_keyword in s_name:
            matches.append(s)

    return matches


def save_report(students, statistics, filename):
    """Write the student results and class statistics to a report file[cite: 2, 3]."""
    if not students or not statistics:
        print("Cannot save report: missing student records or statistics.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("==================================================\n")
            file.write("             STUDENT GRADE ANALYZER REPORT        \n")
            file.write("==================================================\n\n")

            file.write("STUDENT RESULTS:\n")
            file.write(f"{'ID':<12} {'Name':<20} {'Grade':<8} {'Classification':<18} {'Status':<10}\n")
            file.write("-" * 70 + "\n")

            for s in students:
                classification, status = classify_grade(s["grade"])
                file.write(f"{s['student_id']:<12} {s['name']:<20} {s['grade']:<8.2f} {classification:<18} {status:<10}\n")

            file.write("\n" + "=" * 70 + "\n")
            file.write("CLASS STATISTICS:\n")
            file.write(f"Number of students : {statistics['total_students']}\n")
            file.write(f"Class average      : {statistics['average']:.2f}\n")
            file.write(f"Passed count       : {statistics['passed_count']}\n")
            file.write(f"Failed count       : {statistics['failed_count']}\n")
            highest = statistics["highest_student"]
            lowest = statistics["lowest_student"]
            file.write(f"Highest Performing : {highest['name']} - {highest['grade']:.2f}\n")
            file.write(f"Lowest Performing  : {lowest['name']} - {lowest['grade']:.2f}\n")

        print(f"Report successfully saved to '{filename}'.")
    except OSError as error:
        print(f"Error saving report to '{filename}': {error}")


def main():
    """Run the menu-driven Student Grade Analyzer[cite: 2, 3]."""
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter search keyword (ID or Name): ")
            matches = search_student(students, keyword)
            if matches:
                print(f"\nFound {len(matches)} matching record(s):")
                display_students(matches)
            else:
                print("No matching student records found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting Student Grade Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")
            continue


if __name__ == "__main__":
    main()