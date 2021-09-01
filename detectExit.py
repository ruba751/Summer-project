from math import sqrt, atan2, pi,atan
from xml.etree.ElementTree import PI

import numpy as np
from movment import  Drone
import math


def makeRectangle(x,z):
    numOfPoints=len(x)
    mideanX=(float)(sum(x)/numOfPoints)
    mideanZ=(float)(sum(z)/numOfPoints)
    #found the midean point in the cloud

    recDimentions = 0;
    for i in range(numOfPoints):
        recDimentions+=sqrt((x[i]-mideanX)**2+(z[i]-mideanZ)**2)   #some algebra: distance between two points
#     ************************2????????
    recDimentions=recDimentions/numOfPoints
    recDimentions*=2
    rect=[[mideanX-recDimentions,mideanZ+recDimentions],[mideanX+recDimentions,mideanZ+recDimentions],[mideanX+recDimentions,mideanZ-recDimentions],[mideanX-recDimentions,mideanZ-recDimentions]]
    return rect

def deleteWithinRectangleBorders(rectangle,x,z):
    Xs=[]
    Zs=[]
    numOfPoints = len(x)

    for i in range(numOfPoints):

        if(checkInsideRect(rectangle,x[i],z[i])!=1):
            Xs.append(x[i])
            Zs.append(z[i])

    return Xs, Zs

def checkInsideRect(rectangle,x,z):    #for each point we will check if it is located inside the rectangle or not
#check if we recieved a rectangle from the form      _________                 _______
                                            #        |       |         or      \_______\
                                            #        ---------
    upLeft = rectangle[0]
    upRight = rectangle[1]
    downRight = rectangle[2]
    downLeft = rectangle[3]
    if(downLeft[0]-upLeft[0]==0):
        return (x > downLeft[0] and x < upRight[0] and z > downLeft[1] and z < upRight[1])

    #else will check the max and min slope that can fit into the rectangle
    else:
        slope1 = float(downLeft[1] - upLeft[1]) / float(downLeft[0] - upLeft[0])
        slope2 = float(downLeft[1] - downRight[1]) / float(downLeft[0] - downRight[0])
        slope3 = float(upRight[1] - upLeft[1]) / float(upRight[0] - upLeft[0])
        slope4 = float(upLeft[1] - downRight[1]) / float(upRight[0] - downRight[0])

        m1 = float(downLeft[1] - z) / float(downLeft[0] - x)
        m2 = float(upRight[1] - z) / float(upRight[0] - x)
        return (slope2<=m1<=slope1 and slope3<=m2<=slope4)


def findExitQuarterAccordingToDencity(x,z,mideanZ,mideanX):
    #need to calculate which quarter has the max dencity  after we done the cleaning inside the rectangle

    # d = dencity
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0

    sum1x = 0
    sum1z = 0

    sum2x = 0
    sum2z = 0

    sum3x = 0
    sum3z = 0

    sum4x = 0
    sum4z = 0
   
    size=len(x)
    for i in range(size):
        if(x[i] >= mideanX and z[i] >= mideanZ):
            d1 += 1
            sum1x += x[i]
            sum1z += z[i]
        elif(x[i] >= mideanX and z[i] <= mideanZ):
            d2 += 1
            sum2x += x[i]
            sum2z += z[i]
        elif(x[i] <= mideanX and z[i] <= mideanZ):
            d3 += 1
            sum3x += x[i]
            sum3z += z[i]
        elif(x[i] <= mideanX and z[i] >= mideanZ):
            d4+=1
            sum4x+=x[i]
            sum4z+=z[i]
                    
    Max=max([d1,d2,d3,d4])
    if(max==d1):
        return 1,float(sum1x/d1),float(sum1z/d1)
    if(max==d2):
        return 2,float(sum2x/d2),float(sum2z/d2)
    if(max==d3):
        return 3,float(sum3x/d3),float(sum3z/d3)
    else:
        return 4,float(sum4x/d4),float(sum4z/d4)

def getExitAngleFromCenter(centerX, centerZ, mideanX, mideanZ):
     return int(atan(float(centerZ)/float(centerX)  )* 180 / pi)


def moveDrone():
    Drone.move_forward(500)
    Drone.move_forward(200)
def mainyy():                 # this function will retrieve the point cloud and detect the exit of the room
    #also returns to main.py where to go _ in which degree to move
    x, y, z = np.loadtxt('/home/ruba/pointData.csv', unpack=True, delimiter=',')
    size = len(x)
    mideanX = float(sum(x)) / float(size)
    mideanZ = float(sum(z)) / float(size)
    rectangle = makeRectangle(x, z)    # will look at the room from above concidering only X and Z values
    xNew,zNew = deleteWithinRectangleBorders(rectangle,x,z)
    quarterIndex,centerX,centerZ = findExitQuarterAccordingToDencity(xNew,zNew,mideanZ,mideanX)
    angle = getExitAngleFromCenter(centerX, centerZ, mideanX, mideanZ)
    return x,y,z,mideanZ,mideanX,rectangle,xNew,zNew,quarterIndex,angle
