lines = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT']
notWanted = ['B', 'D', 'E', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z']
def filter():
    for i in lines:
        myVar = False
        if any(x in i for x in notWanted):
            myVar = True
        elif len(i) <= 10:
            myVar = True
        elif len(i) > 100:
            myVar = True
        elif ismixed(i):
            myVar = True
        elif i.islower():
            myVar = True
        if myVar == True:
            lines.remove(i)

def ismixed(i):
    return any(c.islower() for c in i) and any(c.isupper() for c in i)

filter()
filter()
filter()
if len(lines) < 3:
    lines = []
print(lines)