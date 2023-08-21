n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    a = int(input("> "))
    numbers.append(a)

even = []
odd = []
multiples_of_5 = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    if i % 2 == 1:
        odd.append(i)
    if i % 5 == 0:
        multiples_of_5.append(i)

print("Even numbers", even)
print("Odd numbers", odd)
print("Multiples of 5", multiples_of_5)
