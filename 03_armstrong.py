n = int(input("Enter a number"))

digits = [i for i in str(n)]

sum_of_cubes = 0
for digit in digits:
    sum_of_cubes += int(digit) ** 3

if sum_of_cubes == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")

# is_armstrong = lambda n: n == sum(int(digit) ** len(str(n)) for digit in str(n))
