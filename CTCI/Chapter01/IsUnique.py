def isUnique(str):
    checker = 0
    for letter in str:
        bit= ord(letter.lower())-ord('a')
        if checker & (1<<bit) > 0:
            return False
        else:
            checker = checker | (1<<bit)
    return True
