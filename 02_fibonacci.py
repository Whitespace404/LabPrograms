n = int(input("Enter the nth number required: "))

a = 1
b = 1
sum_ = 0

for i in range(1, n + 1):
    print(b)
    sum_ = a + b
    b = a
    a = sum_
