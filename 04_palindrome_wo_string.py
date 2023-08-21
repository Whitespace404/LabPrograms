n = int(input("Enter a number: "))
original = n
reversed_number = 0

while n > 0:
    last_digit = n % 10
    reversed_number = (reversed_number * 10) + last_digit
    n //= 10

if reversed_number == original:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
