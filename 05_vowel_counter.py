word = input("Enter a word: ")

vowels = 0
for letter in word:
    if letter in "aeiou":
        vowels += 1

print(vowels)

# print(len(l for l in input() if l in 'aeiou'))
