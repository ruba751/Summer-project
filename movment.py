import threading
from time import sleep

from djitellopy import tello
import os

Drone = tello.Tello();
Drone.connct();

def boot_orbSlam():        # this function will make the orbSlam start working on the drone cam input
    os.chdir('/home/ruba/ORB_SLAM2')
    OrbSlamBoot = './Examples/Monocular/mono_tum Vocabulary/ORBvoc.txt Examples/Monocular/TUM1.yaml'
    os.system(OrbSlamBoot)


def take_shoots():         # this function will activate orb slam and start reconrding the room from diffrent y axis values and angles 
    Drone.streamoff()      # resetting previous connections 
    Drone.streamon()
    run_Orbslam = threading.Thread(target=boot_orbSlam)
    run_Orbslam.start()

    # drone takes off and scans the room
    Drone.send_rc_control(0, 0, 0, 0)
    sleep(1)           
    Drone.takeoff()
    Drone.move_up(80)
    sleep(3)
    angle = 0
    while(angle!=360): 
        Drone.rotate_clockwise(20)
        sleep(4)
        Drone.move_up(25)
        sleep(4)
        Drone.move_down(25)
        sleep(4)
        angle+=20
    Drone.land()
    Drone.streamoff()
    print("reconrding data finished")
    landing_yaw_degree = Drone.get_yaw()     # need this data inorder to ??????offset the starting angle - the drone doensn't land exactly where it tookoff
    run_Orbslam.join()
    return landing_yaw_degree 
