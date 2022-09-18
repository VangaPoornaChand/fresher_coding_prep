
def getUniqueLetter(s):
    
    for i in s:
        if s.count(i) == 1:
            return s.index(i)+1
    else:
        return -1


print(getUniqueLetter("oornachandvanga"))

print(getUniqueLetter("statistics"))

print(getUniqueLetter("hackthegame"))

print(getUniqueLetter("aaaaa"))