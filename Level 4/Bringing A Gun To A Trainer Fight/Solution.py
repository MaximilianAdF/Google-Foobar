#y = kx + m
#if x or y = 0, then k = 0 and m = x | y  => y = x | y
#need to use my position to calculate deltax and delta y


def solution(dimensions, your_position, trainer_position, distance):
    inclinations = inclination(bearings(dimensions=[3,2]))
    path(inclinations, your_position, trainer_position, distance)

def inclination(bearings):
    inclinations = []
    for i in bearings:
        deltaX = i[0]
        deltaY = i[1]
        if deltaX == 0 or deltaY == 0: # Inclination is 0 but constant value is m

            x = deltaX #Constant horizontal value (m)
            y = deltaY #Constant vertical value

            inclinations.append(["const",x,y])

        else:
            #y = kx + m,    m = 0
            k = deltaY/deltaX  #y/x 
            inclinations.append([k])

    print(inclinations)
    return inclinations

def bearings(dimensions):
    x = dimensions[0]
    y = dimensions[1]
    bearings = []

    for i in range(x+1):
        for j in range(y+1):
            if i == 0 and j != 0:
                bearings.append([i,j])
                bearings.append([i,-j])

            elif i != 0 and j == 0:
                bearings.append([i,j])
                bearings.append([-i,j])

            elif [i,j] != [0,0]:
                bearings.append([i,j])
                bearings.append([-i,j])
                bearings.append([i,-j])
                bearings.append([-i,-j])

    return bearings

def path(inclinations, your_position, trainer_position, distance):
    pass
solution([3,2], [1,1], [2,1], 4)

