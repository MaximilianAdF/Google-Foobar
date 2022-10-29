#Turned out to be way too slow and also partially wrong


from fractions import Fraction
from math import sqrt, ceil

def solution(dimensions, your_position, trainer_position, distance):
    hits = 0
    for bearing in possible_bearings(your_position,dimensions,distance):
        if bearing[0] != 0 and bearing[1] != 0: #if not constant
            print(bearing)
            if path(bearing, your_position, trainer_position, dimensions, distance) == True:
                hits += 1

        elif constant(bearing, your_position, trainer_position) == True:
            hits += 1
    return hits

def possible_bearings(your_position,dimensions,distance):
    cp_x = int(ceil(float((your_position[0] + distance)) / dimensions[0]))
    cp_y = int(ceil(float((your_position[1] + distance)) / dimensions[1]))

    bearings = []

    for i in range(0,int(sqrt(dimensions[0]).real)):
        for j in range(0,int(sqrt(dimensions[1]).real)):
            if i == 0 and j != 0:
                bearings.append([i,j])
                bearings.append([i,-j])

            elif i != 0 and j == 0:
                bearings.append([i,j])
                bearings.append([-i,j])

            elif [i,j] != [0,0]:
                bearings.append([i,j])
                bearings.append([-i,j])
                bearings.append([-i,-j])
                bearings.append([i,-j])

    return bearings

def constant(bearing, your_position, trainer_position):
    x0, y0 = your_position[0], your_position[1]
    x1, y1 = trainer_position[0], trainer_position[1]

    if y0 + bearing[1] == y1 and x0 == x1:
        return True
    
    if x0 + bearing[0] == x1 and y0 == y1:
        return True

def intersect(coords, dimensions): #Check corner hits!!!!!!!!!!!
    m = coords[1] - coords[2]*coords[0] #Calculating value of y when x = 0
    y = coords[2]*dimensions[0] + m #Value of y when hit right wall

    if coords[3] == 1:
        if y > dimensions[1]:
            hit = [Fraction((dimensions[1] - m),coords[2]), dimensions[1], -coords[2], 4]
            #Changing direction to 4th quadrant and slope to opposite

        elif y < dimensions[1]:
            hit = [dimensions[0], y, -coords[2], 2]
            #Changing direction to 2nd quadrant and slope to opposite

        elif y == dimensions[1]: #corner hit
            hit = [dimensions[0], dimensions[1], coords[2], 3]
            #Changing direction to 3rd quadrant and slope stays same.

    elif coords[3] == 2:
        if m > dimensions[1]:
            hit = [Fraction((dimensions[1] - m),coords[2]), dimensions[1], -coords[2], 3]
        
        elif m < dimensions[1]:
            hit = [0, m, -coords[2],1]
        
        elif m == dimensions[1]: #corner hit
            hit = [0, dimensions[1], coords[2], 4]

    elif coords[3] == 3:
        if m > 0:
            hit = [0, m, -coords[2], 4]

        elif m < 0:
            hit = [Fraction(-m,coords[2]), 0, -coords[2], 2]
        
        elif m == 0:
            hit = [0, 0, coords[2], 1]

    elif coords[3] == 4:
        if y > 0:
            hit = [dimensions[0], y, -coords[2], 3]

        elif y < 0:
            hit = [Fraction(-m,coords[2]), 0, -coords[2], 1]

        elif y == 0: #corner hit
            hit = [dimensions[0], 0, coords[2], 2]

    return hit

def path(bearing, your_position, trainer_position, dimensions, distance):
    dist = 0
    x = bearing[0]
    y = bearing[1] 

    #Direction of travel (Quadrants)
    if x > 0 and y > 0:
        dir = 1
    elif x < 0 and y > 0:
        dir = 2
    elif x < 0 and y < 0:
        dir = 3
    elif x > 0 and y < 0:
        dir = 4

    coords = [your_position[0],your_position[1],Fraction(y,x),dir]  #coords = [x,y,k]

    while dist < distance:   #Distance shit not working
        if checkHit(trainer_position, coords) == True:
            dist += checkDistance(coords, trainer_position) #Last distance, between previous hit and trainer
            if dist > distance:
                return False
            print(dist, coords,"*")
            return True
        
        tmpCoords = coords[0:] #Copying coords to tmpCoords
        coords = intersect(coords,dimensions)
        dist += checkDistance(tmpCoords, coords)

def checkHit(trainer_position, coords):
    k = coords[2]
    m = coords[1] - k*coords[0] #Function done
    if trainer_position[1] == k*trainer_position[0] + m:
        return True
    else:
        return False

def checkDistance(tmpCoords, coords):
    deltaX = coords[0] - tmpCoords[0]
    deltaY = coords[1] - tmpCoords[1]

    return sqrt(deltaX**2 + deltaY**2).real

#what is going on here?
print(solution([300,275], [150,150], [185,100], 500))
