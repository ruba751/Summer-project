import detectExit
from movment import Drone


def move(distAngle, x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle):
   
    Drone.takeoff()
    Drone.move_up(60)

    if(quarterIndex == 1):
        Drone.rotate_clockwise(angle-distAngle)
    elif (quarterIndex == 2):
        Drone.rotate_clockwise(90-distAngle)
        Drone.rotate_clockwise(abs(angle))
    elif (quarterIndex == 3):
        Drone.rotate_counter_clockwise(distAngle)
        Drone.rotate_counter_clockwise(90)
        Drone.rotate_counter_clockwise(angle)
    elif (quarterIndex == 4):
        Drone.rotate_counter_clockwise(distAngle)
        Drone.rotate_counter_clockwise(90-angle)

    detectExit.moveDrone()
