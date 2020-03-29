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
final = [(final[i:i+3]) for i in range(0, len(final), 3)]
count = []
file = open("codon.txt", "r").read().split("\n")
for x in file:
    for y in final:
        new = x.split(": ")
        if new[0] == y:
            count.append(new[1])

finalCount = {i:count.count(i) for i in count}
print(finalCount)




class DNAAnalyser:

    REPORT_MAPPING_FILENAME = 'codon.tsv'

    def __init__(self):
        pass

    @staticmethod
    def clean_strands(filename):
        with open("input4.txt") as file_in:
            lines = []
            for line in file_in:
                lines.append(line)
        j = 0
        for x in lines:
            lines[j] = x.rstrip("\n")
            j += 1
        def filter():
            for i in lines:
                myVar = False
                if 'B' in i:
                    myVar = True
                elif 'D' in i:
                    myVar = True
                elif 'E' in i:
                    myVar = True
                elif 'F' in i:
                    myVar = True
                elif 'H' in i:
                    myVar = True
                elif 'I' in i:
                    myVar = True
                elif 'J' in i:
                    myVar = True
                elif 'K' in i:
                    myVar = True
                elif 'L' in i:
                    myVar = True
                elif 'M' in i:
                    myVar = True
                elif 'N' in i:
                    myVar = True
                elif 'O' in i:
                    myVar = True
                elif 'P' in i:
                    myVar = True
                elif 'Q' in i:
                    myVar = True
                elif 'R' in i:
                    myVar = True
                elif 'S' in i:
                    myVar = True
                elif 'U' in i:
                    myVar = True
                elif 'V' in i:
                    myVar = True
                elif 'W' in i:
                    myVar = True
                elif 'X' in i:
                    myVar = True
                elif 'X' in i:
                    myVar = True
                elif 'Y' in i:
                    myVar = True
                elif 'Z' in i:
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
        cleaned_list = lines
        return cleaned_list

    def create_strands(self, cleaned_list):
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
            global final = secondstring + temp
        elif secondstring[-3:] == firststring[:3]:
            temp = firststring[3:]
            global final = secondstring + temp
        print("HEREEE")
        print(final)
        result = final
        return result

    def get_amino_acids_report(self, dna_sequence):
        """
        TODO(Part 3): Complete this method
        """
        report = {}
        return report
