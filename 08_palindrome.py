word = input("Enter a word: ")

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# w=input();print(w,"is"[w!=w[::-1]::2],"a palindrome")
