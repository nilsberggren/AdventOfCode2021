
def readInput():
    movement = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            movement.append(line.rstrip())
    return movement


def move(movement):
    x, y = 0, 0
    
    for i in movement:
        print(i[0])
        if i[0] == "f":
            x +=int(i[-1])
        elif i[0] == "d":
            y+=int(i[-1])
        elif i[0] == "u":
            y-=int(i[-1])
        
    print(x)
    print(y)

move(readInput())