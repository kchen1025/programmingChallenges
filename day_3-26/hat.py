
def main():
    personList = []
    guessList = []

    with open("input.txt",'r') as file:
        for i in file:
            personList.append(i.strip())

    number = numHats(personList[1:])
    ##first guess always black because doesn't matter
    guessList.append("Black")
    
    for count in range(1,len(personList)):
        temp = numHats(personList[count+1:])

        if number[0] != temp[0]:
            guessList.append("Black")
        else:
            guessList.append("White")
        number = temp
    print(checkCorrect(personList,guessList))

def numHats(subList):
    #returns a tuple where left is num Black right is num White
    black = 0
    white = 0
    for i in subList:
        if i == 'Black':
            black+=1
        else:
            white+=1
            
    return (black,white)

def checkCorrect(personList,guessList):
    for i,j in zip(personList[1:],guessList[1:]):
        if i != j:
            return False

    return True

main()
