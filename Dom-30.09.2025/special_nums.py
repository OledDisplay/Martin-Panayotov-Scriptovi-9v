numbers = [5, 12, 18, 21, 33, 42, 50, 77, 90]
special_numbers = []
for i in numbers:
    if i > 20 and i % 3 == 0 and i % 5 != 0 :
      special_numbers.append(i)

print(special_numbers)
