import movment
import moveToExit
import detectExit

land_deg=movment.take_shoots()
print('wait for orb_slam and the drone then enter fly....')
x=input()
while x!='fly':    # waiting for orbslam work to be finished - then we will press fly to do the processing on the data
    print('wait')
    x=input()
print(land_deg)
x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle = detectExit.mainyy()
moveToExit.move(land_deg, x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle)
