student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

max = student_scores[0]
min = student_scores[0]

for x in range(len(student_scores)):
    if max < student_scores[x]:
        max = student_scores[x]
    if min > student_scores[x]:
        min = student_scores[x]

print(max)
print(min)