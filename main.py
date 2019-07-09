 #!/usr/bin/python
import os, sys
from wallaby import *
from movement import *
from GCERconstant import*
from GCEReffectors import*
from wait_for_start import*


def main():  
	print("Hello")
  	create_connect()
	enable_servos()
        
	arm_start(50)
	wait_for_start(5)
   	shut_down_in(118)
	msleep(1500)
	arm_up(20)
	forward_to_black(200,0,THRESH)
	forward(200, 300)
	forward_to_black(200,0,THRESH)
	forward(100, 200)
	CW(90,110)
	forward(200, 100)
	forward_to_black(200,0,THRESH)
	forward(200,150)
	CW(100,110)
	line_follow(75, 0, 900, THRESH)
	backward(100, 100)
	line_follow(75, 0, 300, THRESH)
	backward(100, 100)
	line_follow(75, 0, 500, THRESH)
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
	backward(100, 100)
	if side == RIGHT:
		forward(100,250)
		backward(100,50)
		forward(100, 400)
		backward(100,400)
            
	else:
		#CCW(50, 30)
		#forward(100, 450)
		for x in range(6):
			CCW(50,60/10)
			forward(50,500/5)
		for x in range(6):
			backward(50,500/5)
			CW(50,60/10)
		forward(100, 50)
                
	CCW(50, 90)
	#forward(50, 200)
	#backward_to_black(200, 0, THRESH)
	backward(100, 200)
	arm_ready(20)
	forward_to_black(100, 0, THRESH)
	CCW(50,2)
	forward( 50, 250)
	arm_down(20)
	backward_to_black(50, 0, THRESH)
	drive_to_bump(100)
	arm_start(20)
               
	forward_to_black(100, 0,THRESH)
	forward(50, 100)
	CW(50, 90)
	if side == RIGHT:
		line_follow(100,0,400,THRESH)
		backward(100,400)
            
	else:
		#CCW(50, 30)
		#forward(100, 450)
		for x in range(6):
			CCW(50,30/10)
			forward(50,450/5)
		for x in range(6):
			backward(50,450/5)
			CW(50,30/10)
	CCW(100,180)
	forward(100,400)
	CW(100,90)
	backward(100,400)
	arm_ready(50)
	CCw(100,2)
	forward_to_black(100,0,THRESH)
	forward(100,400)
	arm_down(20)
	backward_to_black(100,0,THRESH)
	drive_to_bump(100)
	arm_up(50)
	forward_to_black(100,0,THRESH)
	CW(50,90)
	if side == RIGHT:
		line_follow(100,0,550,THRESH)
		backward(100,550)
            
	else:
	
		for x in range(6):
			CCW(50,30/10)
			forward(50,450/5)
		for x in range(6):
			backward(50,450/5)
			CW(50,30/10)
	


	#CCW(100,90)
	#turn_CW_to_black(100,0,THRESH)
	#line_follow(100,0,300,THRESH)
	#CW(100,90)
	#backward(100,200)
	#arm_ready(20)
	#forward(50,400)
	#arm_down(20)
	#backward_to_black(50,0,THRESH)
   	disable_servos()
                
	
	
                
	#CCW(50,95)
	#drive_to_bump(10
	#CW(50, 5)
	#forward_to_black(100, 0, THRESH)
	#CCW(50, 10)
	#forward(100, 350)
	#turn_to_gap()
	#backward_to_black(100, 0, THRESH)
	
	
	#forward(50, 350)
	#arm_down(20)
	#drive_to_bump(100)
	#forward(50, 10)
	#arm_up(20)
	#CCW(50, 90)
	#forward(100, 275)
	#CW(50, 90)
	#arm_ready(20)
	#forward(100, 100)
	#forward_to_black(100, 0, THRESH)
	#forward(100, 320)
	
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
                

                
                
	

	

	