from time import sleep
import autopy
import	random
import math



def generatetuple(tup1,tup2):
	xspace = (tup2[0] - tup1[0])/800
	yspace = (tup2[1] - tup1[1])/800
	alist = [[tup1[0],tup1[1]],]
	for i in range(800):
		alist.append([xspace * i + tup1[0], yspace * i + tup1[1]])	
	return alist

def gogogo():
	x=random.randint(math.ceil(200/1.525),math.ceil(2200/1.525))
	y=random.randint(math.ceil(200/1.525),math.ceil(1200/1.525))
	clocation = autopy.mouse.location()
	alist = generatetuple((clocation[0]/1.56,clocation[1]/1.56),(x,y))
	for [j,k] in alist:
		sleep(0.0000000001)
		a = int(math.ceil(j))
		b = int(math.ceil(k))
		autopy.mouse.move(a,b)
	
	
print(" Shengfu is temporary away, please call his number")
while True:
	gogogo()

