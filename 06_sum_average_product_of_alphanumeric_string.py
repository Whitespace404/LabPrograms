string = input("Enter an alphanumeric string: ")

sum_ = 0
product = 1
digits = 0

for letter in string:
    if letter.isnumeric():
        sum_ += int(letter)
        product *= int(letter)
        digits += 1

average = sum_ / digits

print("Sum=", sum_)
print("Average=", average)
print("Product=", product)
