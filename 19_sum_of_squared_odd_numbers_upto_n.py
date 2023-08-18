n = int(input("Enter the limit: "))

sum_ = 0

for i in range(1, n+1, 2):
    sum_ += i**2

print(sum_)
