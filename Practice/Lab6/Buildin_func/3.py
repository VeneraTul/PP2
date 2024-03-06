word=input()
word1=''.join(reversed(word))
if word==word1:
    print("is palindrome")
else:
    print("is not palindrome")
