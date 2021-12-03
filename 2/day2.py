
def readInput():
    movement = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            movement.append(line.rstrip())
    return movement


def one(movement):
    x, y = 0, 0
    
    for i in movement:

        if i[0] == "f":
            x +=int(i[-1])
        elif i[0] == "d":
            y+=int(i[-1])
        elif i[0] == "u":
            y-=int(i[-1])
        
    return x*y


def two(movement):
    x, y = 0, 0
    aim = 0

    for i in movement:

        if i[0] == "f":
            x +=int(i[-1])
            y +=aim*int(i[-1])
        elif i[0] == "d":
            aim+=int(i[-1])
        elif i[0] == "u":
            aim-=int(i[-1])
    
    return x*y

#Part 1
print(one(readInput()))

#Part 2
print(two(readInput()))