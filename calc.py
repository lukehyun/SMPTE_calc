from timecode import Timecode
import time

fr = input("frame : ");
ti = input("time : ");
ti = int(ti)


#test_tc = Timecode(fr, ti)

test_tc = Timecode('29.97', '00:00:10:00')

#Forcibly printing framerate as if frame_number was set to 0

print(test_tc.frames - 1)

