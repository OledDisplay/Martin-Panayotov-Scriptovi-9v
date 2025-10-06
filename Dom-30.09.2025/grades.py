grades = [95, 82, 67, 54, 100, 73, 88, 42]

excellent = []
good = []
passed = []
failed = []

for grade in grades:
    if grade >= 90:
        excellent.append(grade)
    elif grade >= 70:
        good.append(grade)
    elif grade >= 50:
        passed.append(grade)
    else:
        failed.append(grade)

print("Excellent:", excellent)
print("Good:", good)
print("Pass:", passed)
print("Fail:", failed)
