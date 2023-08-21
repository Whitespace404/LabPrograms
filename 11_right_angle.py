l = input("Enter a word")

for i in range(len(l) + 1):
    for j in range(i):
        print(l[j], end="")
    print()
