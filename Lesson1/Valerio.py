scores = [85, 71, 99, 88, 77]

print("Student Scores:")

for score in scores:
    print(score)

print()

passed_count = 0
failed_count = 0

total_score = sum(scores)
avg_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

for index in range(len(scores)):
    score = scores[index]

    if score >= 75:
        if score >= 90:
            remark = "Excellent"
        elif score >= 80:
            remark = "Very Good"
        else:
            remark = "Good"

        print(f"Student {index + 1}: {score} - {remark} - Passed")
        passed_count += 1
    else:
        print(f"Student {index + 1}: {score} - Failed")
        failed_count += 1

print()

print(f"Total Score: {total_score}")
print(f"Average Score: {int(avg_score)}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")