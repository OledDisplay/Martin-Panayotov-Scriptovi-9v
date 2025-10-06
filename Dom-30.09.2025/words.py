words = ["level", "python", "radar", "java", "civic", "kotlin", "refer"]
palindroms = []
for i in words:
    p = 0
    for z in range(len(i)):
        if z >= len(i) // 2:
            if i[z] != i[len(i) - 1 - z]:
                break
        p += 1
    if p == len(i):
        palindroms.append(i)

print(palindroms)
