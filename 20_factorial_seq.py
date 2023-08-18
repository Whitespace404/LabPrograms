n = int(input("Enter the limit: "))

sum_ =  0
for i in range(n):
    factorial = 1

    for j in range(1, i + 1):
        factorial *= j

    sum_ += 1/factorial

print(sum_)
