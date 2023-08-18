e = int(input("Enter the number of names: "))
names = []

for i in range(e):
    n = input("> ")
    names.append(n)

voweless_names = []

for name in names:
    has_vowel = False

    for letter in name:
        if letter in "aeiou":
            has_vowel = True
            break
    else:
        voweless_names.append(name)

print(voweless_names)
            


            
