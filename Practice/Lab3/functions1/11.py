def palindrome_words(string):
    k = string[::-1]
    if k == string:
        return True
    return False
print(palindrome_words("madam"))