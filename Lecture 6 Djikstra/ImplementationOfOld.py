from math import fabs
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString, Point

def sortyStuff(line):
    return line[1][0]
class Node:
    def __init__(self, data):
        self.data = data
        self.goal = None
        self.children = []
        self.cost = []
        self.route = []
        self.accumCost = 0
        self.backPointer = None
        self.x = None
        self.y = None
    def addChild(self, child, costFloat):
        self.children.append(child)
        self.cost.append(costFloat)
x1, y1 = [0, 12], [0, 0]
x2, y2 = [0, 0], [0, 15]
x3, y3 = [0, 12], [15, 15]
x4, y4 = [12, 12], [0, 15]
worldX = [x1,x2,x3,x4]
worldY = [y1,y2,y3,y4]
class area:
    def __init__(self):
        self.placement = 0
        self.middle = []
        self.rightPath = False
        self.leftPath = False
        self.connections = 0
box = [[1,1],[3,1],[2,2],[1,3]]
boxX = [3,1,4,4,3]
boxY = [3,1,5,2,3]
Obstacle = area()
Obstacle.middle = [(boxX[0]+boxX[1]+boxX[2]+boxX[3])/4,(boxY[0]+boxY[1]+boxY[2]+boxY[3])/4]
plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, marker = 'o')
print(type(box[0][0]))
plt.plot(boxX,boxY, marker="H")
lines = []
for x in range(len(boxX)):
    countLeft = 0
    countRight = 0
    print("X :: "+str(x))
    #print([x1[0],boxX[x]],[boxY[x],boxY[x]])
    for y in range(len(boxX)-1):
        line1 = LineString([(x1[0],boxY[x]), (boxX[x],boxY[x])])
        line2 = LineString([(boxX[y],boxY[y]), (boxX[y+1],boxY[y+1])])
        int_pt = line1.intersection(line2)
        print(int_pt)
        if str(int_pt) == "LINESTRING EMPTY":
            countLeft = countLeft + 1

        line1 = LineString([(x4[0],boxY[x]), (boxX[x],boxY[x])])
        line2 = LineString([(boxX[y],boxY[y]), (boxX[y+1],boxY[y+1])])
        int_pt = line1.intersection(line2)
        print(int_pt)
        if str(int_pt) == "LINESTRING EMPTY":
            countRight = countRight + 1
    if (countLeft > 1):
        lines.append([[x1[0],boxX[x]],[boxY[x],boxY[x]]])
    if (countRight > 1):
        lines.append([[x4[0],boxX[x]],[boxY[x],boxY[x]]])
    countLeft, countRight = 0, 0
for x in range(len(lines)):
    plt.plot(lines[x][0],lines[x][1], color="#88ff88", marker="p")

lines.sort(key=sortyStuff)
area_centers = [[(x1[0]+x1[1])/2,(y1[0]+lines[0][1][0])/2]]

areas = []
if any(boxY) != 0:
    print("FUCK")
    areas.append(area())
    areas[0].placement = 2
    areas[0].middle = [(x1[0]+x1[1])/2,lines[0][0][1]/2]
    print(areas[0].middle)
for x in range(len(lines)):
    middleX = (lines[x][0][0]+lines[x][0][1])/2
    nextLine = None
    if x == len(lines) - 1:
        continue
    for y in range(len(lines[x:])):
        if lines[x+y][0][0] == lines[x][0][0] and lines[x+y][1] != lines[x][1]:
            areas.append(area())
            middleY = (lines[x][1][0] + lines[x+y][1][0])/2
            areas[-1].middle=[middleX, middleY]
            if middleX > Obstacle.middle[0]:
                areas[-1].placement = 0
            else:
                areas[-1].placement = 1
            area_centers.append([middleX,middleY])
            plt.text(middleX, middleY, str(x), fontsize=12)
            break
areas.append(area())
areas[-1].middle = [(x1[0]+x1[1])/2, (lines[-1][0][1]+y3[1])/2]
areas[-1].placement = 2
nodes = []
for x in range(len(areas)-1):
    for y in range (len(areas[x:])):
        
        if areas[x].middle == areas[y+x].middle:
            continue
        if areas[x].placement == areas[y+x].placement or areas[x].placement == 2 or areas[x+y].placement == 2:
            if (areas[x].connections > 1 or areas[x+y].connections > 1):
                continue
            if (areas[x].placement == 2):
                if (areas[x+y].placement == 1):
                    if areas[x].leftPath:
                        continue
                    else:
                        areas[x].leftPath = True
                elif(areas[x+y].placement == 0):
                    if (areas[x].rightPath):
                        continue
                    else:
                        areas[x].rightPath = True
            elif (areas[x+y].placement == 2):
                if (areas[x].placement == 1):
                    if areas[x+y].leftPath:
                        continue
                    else:
                        areas[x+y].leftPath = True
                elif(areas[x].placement == 0):
                    if (areas[x+y].rightPath):
                        continue
                    else:
                        areas[x+y].rightPath = True
            areas[x].connections = areas[x].connections + 1
            areas[x+y].connections = areas[x+y].connections + 1
            nodes.append(Node(x))
            nodes[x]
            plt.plot([areas[x].middle[0],areas[y+x].middle[0]],[areas[x].middle[1],areas[y+x].middle[1]],color="red", marker="p")

plt.show()


