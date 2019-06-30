#!/usr/bin/python
import os, sys
from wallaby import *
from GCERconstant import *



#Created Wednesday, February 6th, 2019. Creators: Dhruv Pal and Aditya Patra.

#Function: backward
#Description: move backward at a certain speed a certain distance
#Arguments:
	#speed = speed the robot moves
	#mm = distance in mm to move

def backward(speed, mm):
   	
	set_create_distance(0);
	create_drive_straight(speed);
	while(get_create_distance() < mm):
		pass
  	create_drive_straight(0)

#Function: forward
#Description: move forward at a certain speed a certain distance
#Arguments:
	#speed = speed the robot moves
	#mm = distance in mm to move

def forward (speed, mm):
    
	set_create_distance(0)
	create_drive_direct(-speed, -speed)
	while(get_create_distance() > -mm):
		pass
 	create_drive_straight(0)	
	set_create_distance(0)

def CCW(speed, angle):
    
	set_create_total_angle(0)
	create_spin_CW(speed)
	while(get_create_total_angle() >= -angle):
		pass
 	create_spin_CW(0)
        
def CW(speed, angle):
    
	set_create_total_angle(0)
	create_spin_CCW(speed)
	while(get_create_total_angle() < angle):
		pass
	create_spin_CCW(0)
	
def forward_to_black(speed, port, thresh):
	create_drive_straight(-speed)
	while(analog(port) <= thresh):
		pass
 	create_drive_straight(0)

def backward_to_black(speed,port,thresh):
	create_drive_straight(speed)
	while(analog(port) <= thresh):
		pass
  	create_drive_straight(0)
            
def turn_CW_to_black(speed, port, thresh):
	create_spin_CW(speed)
	while(analog(port) <= thresh):
		pass
 	create_spin_CW(0)

def turn_CCW_to_black(speed, port, thresh):
	create_spin_CCW(speed)
	while(analog(port) <= thresh):
		pass
 	create_spin_CCW(0)
            
def drive_to_bump(speed):
	create_drive_straight(speed)
	while get_create_lbump()== 0 and get_create_rbump()==0:
		pass
 	create_drive_direct(0,0)
            
def line_follow(speed, port, distance, thresh):
	set_create_distance(0)
	while (get_create_distance() > -distance):
		if analog(port)>= THRESH:
			create_drive_direct(-speed, -(speed-25))
		else:
			create_drive_direct(-(speed-25), -speed)
	create_drive_direct(0,0)
                
def turn_to_gap():
	create_spin_CCW(30)
	while analog(4) > 2000:
		pass
	create_drive_direct(0,0)