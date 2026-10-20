raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,"
]

PASSING_GRADE = 75

student_scores = {}

for record in raw_records:
    fields = record.split(",")

    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]

    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores

print("\nORGANIZED STUDENT RECORDS")
print("-" * 35)

for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")

ranking = []

passed_count = 0
failed_count = 0
sum_of_averages = 0

for name, scores in student_scores.items():
    if not scores:
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    if average >= PASSING_GRADE:
        remark = "Passed"
        passed_count += 1
    else:
        remark = "Failed"
        failed_count += 1

    sum_of_averages += average

    ranking.append((average, name, highest_score, lowest_score, remark))

ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print(f"{'Rank':<6} {'Name':<10} {'Average':<10} {'Highest':<9} {'Lowest':<9} {'Remark':<8}")
print("-" * 60)

for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<6} {name:<10} {average:<10.2f} {highest_score:<9} {lowest_score:<9} {remark:<8}")

total_students = len(ranking)
class_average = sum_of_averages / total_students if total_students > 0 else 0

highest_student = ranking[0] if ranking else (0, "N/A", 0, 0, "")
lowest_student = ranking[-1] if ranking else (0, "N/A", 0, 0, "")

print("\nCLASS SUMMARY")
print("-" * 25)
print(f"Number of Students: {total_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Class Average: {class_average:.2f}")
print(f"Highest: {highest_student[1]} - {highest_student[0]:.2f}")
print(f"Lowest: {lowest_student[1]} - {lowest_student[0]:.2f}")