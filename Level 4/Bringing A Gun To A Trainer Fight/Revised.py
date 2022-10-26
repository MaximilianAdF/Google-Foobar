def solution(dimensions, your_position, trainer_position, distance):
    pass

def possible_bearings(dimensions):
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
bearings = possible_bearings([3,2])

def steps(bearings, your_position):
    x0 = your_position[0]
    y0 = your_position[1]
    steps = []
    print(bearings)
    for i in bearings:
        x = x0 + i[0]
        y = y0 + i[1]
        steps.append([x,y])
    return steps
print(steps(bearings, [1,1]))

def intersect():
    pass
