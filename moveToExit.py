import detectExit
from movment import Drone


def move(distAngle, x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle):

    Drone.takeoff()
    Drone.move_up(60)

    print(Drone.get_battery())
    if distAngle<0:
        Drone.rotate_clockwise(abs(distAngle))
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

# rotating the drone angle acordingly
    detectExit.moveDrone()
