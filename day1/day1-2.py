numberDict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
#z,o,t,f,s,e,n
def matchWord(substr, numDict):
    numWords = numDict.keys()
    
sum = 0
with open('input.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        firstseenflag = False
        firstseendigit = 0
        lastseendigit = -1
        number = 0
        for i in range(len(line)):
            c = line[i]
            if c.isnumeric():
                if firstseenflag:
                    lastseendigit = int(c)
                else:
                    firstseenflag = True
                    firstseendigit = int(c)
    
        if lastseendigit == -1:
            number = firstseendigit*11
        else:
            number = firstseendigit*10 + lastseendigit
        print(number)
        sum = sum + number
        line = reader.readline()
print(sum)