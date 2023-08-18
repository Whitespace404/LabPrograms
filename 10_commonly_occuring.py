sentence = input("Enter a sentence: ").lower()
words = sentence.split()

common = []

for word in words:
    if words.count(word) > 1:
        if word not in common:
            common.append(word)

print(common)
