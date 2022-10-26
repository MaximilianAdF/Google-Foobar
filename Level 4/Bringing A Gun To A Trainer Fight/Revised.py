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

#print(bearings)
"""
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
"""
def inclination(bearing):
    x = bearing[0]
    y = bearing[1]

    k = y/x #slope

    return k


def path(bearings, your_position):
    paths = []
    for i in bearings:
        if i[0] != 0 and i[1] != 0 and [i[0],i[1]] != your_position:  #If not same position or constant
            slope = [i[0],i[1],inclination([i[0],i[1]])]
            intersect(slope,[1,1],[3,2])

        else:
            pass
            #deal with constants.

def intersect(slope, your_position, dimensions):
    x = slope[0]
    y = slope[1]
    
    if x < 0 and y > 0:
        # y = kx + m
        # m = y - kx [1,1] => m = 1 - k
        m = 1 - slope[2] #(=y) when x = 0 (When line is hit)
        x = your_position[0] #steps to the left required to hit x = 0

        if m < dimensions[1]:
            #Hit on left wall (x = 0) at (0,m)
            hit = [0,m]
        
        elif m > dimensions[1]:
            #Hit on top wall (y = dimensions[1])
            # dimensions[1] = kx + m => x = (dimensions[1] - m)/k
            hit = [(dimensions[1] - m)/slope[2], dimensions[1]]
    
        elif m == dimensions[1]: #Corner hit
            hit = [0,dimensions[1]]

        #Second hit???
        print(hit)
        



    elif x < 0 and y < 0:
        #print(slope, "+")
        pass
    elif x > 0 and y > 0:
        #print(slope, "-")
        pass
    elif x > 0 and y < 0:
        #print(slope, "/")
        pass

path(bearings, [1,1])



def checkHit(your_position, trainer_position, distance):
    pass
