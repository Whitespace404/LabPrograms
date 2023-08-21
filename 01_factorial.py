n = int(input("Enter a number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(factorial)

# f=lambda n:1 if n<1 else n*f(n-1);print(f(int(input())))
