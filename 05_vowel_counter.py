# print(len([w for w in input() if w in "aeiou"]))

word = input('Enter a word: ')

vowels = 0
for letter in word:
    if letter in "aeiou":
        vowels += 1

print(vowels)
