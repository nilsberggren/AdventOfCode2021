
def readInput():
    diagnostics = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            diagnostics.append(line.rstrip())
    return diagnostics


def one(diagnostics):
    bitList1 = []
    bitList2 = []
    bitList3 = []
    bitList4 = []
    bitList5 = []
    bitList6 = []
    bitList7 = []
    bitList8 = []
    bitList9 = []
    bitList10 = []
    bitList11 = []
    bitList12 = []

    gammaRate = ""
    epsilonRate = ""

    counter = 0

    #loop through the input diagnostics and append to the bitlists
    #every column in the input is converted to a corresponding bitlist
    #ie column 1 is bitlist1 and so on
    while counter < len(diagnostics) :
        subCounter = 0
        subList = (list(diagnostics[counter]))

        while subCounter < len(subList) :

            if subCounter == 0 :
                bitList1.append(subList[subCounter])
            elif subCounter == 1 :
                bitList2.append(subList[subCounter])
            elif subCounter == 2 :
                bitList3.append(subList[subCounter])
            elif subCounter == 3 :
                bitList4.append(subList[subCounter])
            elif subCounter == 4 :
                bitList5.append(subList[subCounter])
            elif subCounter == 5 :
                bitList6.append(subList[subCounter])
            elif subCounter == 6 :
                bitList7.append(subList[subCounter])
            elif subCounter == 7 :
                bitList8.append(subList[subCounter])
            elif subCounter == 8 :
                bitList9.append(subList[subCounter])
            elif subCounter == 9 :
                bitList10.append(subList[subCounter])
            elif subCounter == 10 :
                bitList11.append(subList[subCounter])
            elif subCounter == 11 :
                bitList12.append(subList[subCounter])
            subCounter += 1
        counter += 1

    #calculate the gammaRate using the gammaBitCheck function
    gammaRate += str(gammaBitCheck(bitList1))
    gammaRate += str(gammaBitCheck(bitList2))
    gammaRate += str(gammaBitCheck(bitList3))
    gammaRate += str(gammaBitCheck(bitList4))
    gammaRate += str(gammaBitCheck(bitList5))
    gammaRate += str(gammaBitCheck(bitList6))
    gammaRate += str(gammaBitCheck(bitList7))
    gammaRate += str(gammaBitCheck(bitList8))
    gammaRate += str(gammaBitCheck(bitList9))
    gammaRate += str(gammaBitCheck(bitList10))
    gammaRate += str(gammaBitCheck(bitList11))
    gammaRate += str(gammaBitCheck(bitList12))

    #calculate the epsilonRate using the epsilonBitCheck function
    epsilonRate += str(epsilonBitCheck(bitList1))
    epsilonRate += str(epsilonBitCheck(bitList2))
    epsilonRate += str(epsilonBitCheck(bitList3))
    epsilonRate += str(epsilonBitCheck(bitList4))
    epsilonRate += str(epsilonBitCheck(bitList5))
    epsilonRate += str(epsilonBitCheck(bitList6))
    epsilonRate += str(epsilonBitCheck(bitList7))
    epsilonRate += str(epsilonBitCheck(bitList8))
    epsilonRate += str(epsilonBitCheck(bitList9))
    epsilonRate += str(epsilonBitCheck(bitList10))
    epsilonRate += str(epsilonBitCheck(bitList11))
    epsilonRate += str(epsilonBitCheck(bitList12))

    print(int(gammaRate, 2))
    print(int(epsilonRate, 2))

    #convert final gammaRate and epsilonRate to int and decimal from binary
    #multiply it and return it to get energy consumption of submarine
    return(int(gammaRate, 2)*int(epsilonRate, 2))

def gammaBitCheck(bitList) :
    zero, one, bit = 0, 0, 0
    #check if 0 or 1 is most common in bitlist
    for i in bitList :
        if i == "0" :
            zero += 1
        elif i == "1" :
            one += 1
    if zero > one :
        bit = 0
    elif zero < one :
        bit = 1
    return(bit)

def epsilonBitCheck(bitList) :
    zero, one, bit = 0, 0, 0
        #check if 0 or 1 is most common in bitlist
    for i in bitList :
        if i == "0" :
            zero += 1
        elif i == "1" :
            one += 1
    if zero > one :
        bit = 1
    elif zero < one :
        bit = 0
    return(bit)


#Part 1
print(one(readInput()))