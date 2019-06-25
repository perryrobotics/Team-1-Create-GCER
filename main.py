#!/usr/bin/python
import os, sys
from wallaby import *
from movement import *
from GCERconstant import*
from GCEReffectors import*
from wait_for_start import*


def main():  
  	create_connect()
	enable_servos()
        
	arm_start(50)
	CCW(100,95)
	forward_to_black(300,0,THRESH)
	forward(300, 300)
	forward_to_black(300,0,THRESH)
	forward(100, 150)
	CW(90,105)
	forward_to_black(300,0,THRESH)
	forward(100,150)
	CW(100,90)
	line_follow(100,0,1400,THRESH)
	#==============================CAMERA CODE========================================= 
	side = RIGHT
	print ("Determining burning building!")
	camera_open()
        
	for x in range(15):
		camera_update()
		msleep(50)

	for x in range(15):
		camera_update()
		if get_object_count(YELLOW) > 0:
			size = get_object_area(YELLOW, 0)
			red = get_object_count(RED)
			if size > 300 and red >0:
				side = LEFT
				print("SIDE LEFT!!!!")
		msleep(50)
	#==============================CAMERA CODE========================================= 		
	camera_close()	
	if side == RIGHT:
		forward(100,500)
		backward(100,500)
            
	else:
		#CCW(50, 30)
		#forward(100, 450)
		for x in range(6):
			CCW(50,30/10)
			forward(50,450/5)
		for x in range(6):
			backward(50,450/5)
			CW(50,30/10)
                
	CCW(50,95)
	drive_to_bump(100)
	arm_ready(20)
	CW(50, 5)
	forward_to_black(100, 0, THRESH)
	CCW(50, 5)
	forward(50, 350)
	arm_down(20)
	drive_to_bump(100)
	forward(50, 10)
	arm_up(20)
	CCW(50, 90)
	forward(100, 275)
	CW(50, 90)
	arm_ready(20)
	forward(100, 100)
	forward_to_black(100, 0, THRESH)
	forward(100, 320)
	
		#backward(100, 450)
		#CW(50,30)
		
       	
	
        
        
        
        
        
	#CW(50,30)
	#forward(100, 50)
	#CW(50,30)
	#forward(100, 50)
	#CW(50,60)
	#forward(100, 50)
	#CW(50,30)
	#forward(100, 400)
	#backward(100, 200)
	#CCW(50, 60)
	#forward(100,300)
	#backward_to_black(100,0,THRESH)
	#forward(100, 100)
	#backward_to_black(100,0,THRESH)
	#CCW(50,90)
	
		
        

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main()