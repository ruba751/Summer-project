import movment
import moveToExit

land_deg=movment.take_shoots()
print('wait for orb_slam and the drone then enter fly....')
x=input()
while x!='fly':
    print('wait')
    x=input()
print(land_deg)
x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle = detectExit.mainyy()
moveToExit.move(land_deg, x, y, z, mideanZ, mideanX, rectangle, xNew, zNew, quarterIndex, angle)
