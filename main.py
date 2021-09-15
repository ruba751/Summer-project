import detectExit
import movment
import moveToExit

land_deg=movment.take_shoots()                   #here we will get data into orb-slam2 by flying the drone up and down rotating 360 degree - screening the whole room
print('wait for orb_slam and the drone then enter fly....')
x=input()                                        # we will wait untill orb-slam2 finishes his work, then we have to press "fly" - to countinue 
while x!='fly':
     print('wait')
     x=input()
print(land_deg)
x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle = detectExit.mainyy()       #after getting the data we will manupilate the points-cleaning #points within the room ...
print(quarterIndex)

moveToExit.move(land_deg, x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle)  #and finally we will move the drone towards the exit point we found previously

