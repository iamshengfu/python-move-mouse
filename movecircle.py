import math
import win32api
import win32con
i = win32api.GetSystemMetrics(0)
j =  win32api.GetSystemMetrics(1)
a = [[int((math.cos(x / 180 * math.pi)* 50 +500)*65535/i),int((math.sin(x / 180 * math.pi)* 50 +500)*65535/j)] for x in range(360)]

while True:
	for pos in a:
		x= pos[0]
		y= pos[1]
		win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,x,y)
		win32api.Sleep(2)