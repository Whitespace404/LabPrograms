sentence = input("Enter a sentence")
words = sentence.split()

unique_words = []
for word in words:
    if sentence.count(word) == 1:
        unique_words.append(word)

largest_word = ""

for word in unique_words:
    if len(word) > len(largest_word):
        largest_word = word

print(largest_word)
