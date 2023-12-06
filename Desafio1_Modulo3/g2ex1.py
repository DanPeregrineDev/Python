def isSame(word):
    for letter in word:
        if letter != word[0]:
            return False
    return True

print(isSame("aaab"))