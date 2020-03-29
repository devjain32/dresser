cleaned_list = ['AGTGGGGGGGGG', 'AAACCCAATTT', 'TTTACACAGCT', 'GCTGGGCCCAGT']

lines = cleaned_list
firststring = ""
secondstring = ""
for x in lines:
    for y in lines:
        if x[-3:] == y[:3]:
            new = y[3:]
            firststring = x + new
for x in lines:
    for y in lines:
        if x[-3:] == y[:3]:
            new = y[3:]
            secondstring = x + new
            lines.remove(x)
            lines.remove(y)
if secondstring[-3:] == firststring[:3]:
    temp = firststring[3:]
    final = secondstring + temp
elif secondstring[-3:] == firststring[:3]:
    temp = firststring[3:]
    final = secondstring + temp
print(final)