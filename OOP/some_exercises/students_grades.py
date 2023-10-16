# find the students having the second-lowest grade

students_dict = {}

for _ in range(int(input())):
    name = input()
    score = float(input())

    if name not in students_dict:
        students_dict[name] = 0

    students_dict[name] = score

min_score = min(students_dict.values())

grade_dict = {}

for key in students_dict:
    if students_dict[key] != min_score:
        grade_dict[key] = students_dict[key]

min_score = min(grade_dict.values())
last = []

for key in grade_dict:
    if grade_dict[key] == min_score:
        last.append(key)

print("\n".join(sorted(last)))

