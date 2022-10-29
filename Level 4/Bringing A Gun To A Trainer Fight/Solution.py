from math import ceil, sqrt, atan2

def solution(dimensions, your_position, trainer_position, distance):
    max_x = float(your_position[0] + distance) 
    max_y = float(your_position[1] + distance)

    #How many times we can mirror the "box" in x, y directions.
    mirror_x = int(ceil(max_x/dimensions[0]))
    mirror_y = int(ceil(max_y/dimensions[1]))
    
    #Quadrant 1 - positions
    Q1 = []
    for x in range (mirror_x):
        for y in range(mirror_y):
            temp_player = [your_position[0] + x*dimensions[0], your_position[1] + y*dimensions[1], "p"]
            temp_trainer = [trainer_position[0] + x*dimensions[0], trainer_position[1] + y*dimensions[1], "t"]

            if x % 2 != 0:
                    temp_player[0] = temp_player[0] - (2 * your_position[0]) + dimensions[0]
                    temp_trainer[0] = temp_trainer[0] - (2 * trainer_position[0]) + dimensions[0]
            if y % 2 != 0:
                    temp_player[1] = temp_player[1] - (2 * your_position[1]) + dimensions[1]
                    temp_trainer[1] = temp_trainer[1] - (2 * trainer_position[1]) + dimensions[1]
            Q1.append(temp_player)
            Q1.append(temp_trainer)
    
    #Quadrant 2 - positions
    Q2= [[-x,y,k] for [x,y,k] in Q1]

    #Quadrant 3 - positions
    Q3 = [[-x,-y,k] for [x,y,k] in Q1]

    #Quadrant 4 - positions
    Q4 = [[x,-y,k] for [x,y,k] in Q1]

    #Distances from your_position
    positions = [[x, y, dist(your_position, [x, y]), k] for [x, y, k] in Q1 + Q2 + Q3 + Q4]

    #Filter for distances: Remove positions that are too far away and sort by distance
    positions = filter(lambda x: x[2] <= float(distance), positions)
    positions = sorted(positions, key=lambda x: x[2])
    
    #Filter for angles: Remove positions that are same angle
    angles = {}
    for i in positions[1:]:
        agl = angle(your_position, [i[0], i[1]])
        if agl not in angles:
            angles[agl] = i
    
    return sum(1 for pos in angles.values() if pos[3] == "t")

#Using atan2 to get angle between horizontal plane and the line that connects your_position and the trainers position
def angle(a,b):
    return atan2((b[1] - a[1]), (b[0] - a[0]))

#Pythagoras theorem to get distance between two points
def dist(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2).real

print(solution([3, 2], [1, 1], [2, 1], 4))
    
