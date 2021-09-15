import detectExit
from movment import Drone


def move(distAngle, x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle):    #we will rotate the drone to an angle which it will fly in a direct way from it's location to the exit point of the room

    Drone.takeoff()
    Drone.move_up(60)

    if distAngle<0:
        Drone.rotate_clockwise(abs(distAngle))  #dist angle is the error angle- at first we concidered the start angle as our origin but after flying 360 degree and scanning the room- the drone won't land on the origin point, so we will calculate the diffrence between the origin and the land angle degree and thus make things right
    else:
        Drone.rotate_counter_clockwise(distAngle)
    if(quarterIndex == 1):
        Drone.rotate_clockwise(90-angle)
    elif(quarterIndex == 2):
        Drone.rotate_clockwise(90-angle)
    elif(quarterIndex == 3):
        Drone.rotate_counter_clockwise(90+angle)
    elif(quarterIndex == 4):
        Drone.rotate_counter_clockwise(90+angle-8)     # a constant value - for errors

# rotating the drone angle acordingly and then fly in a direct way
    detectExit.moveDrone()
