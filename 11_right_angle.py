l = int(input("Enter the length of the triangle: "))

for i in range(l + 1):
    for j in range(i):
        print("*", end='')
    print()
