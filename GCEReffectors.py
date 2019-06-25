#!/usr/bin/python
import os, sys
from wallaby import *
from GCERconstant import *

def move_servo_slow(port, current_pos, end_pos,step):
	if end_pos < current_pos:
		step = -step
	for pos in range(current_pos, end_pos, step):
		set_servo_position(port, pos)
  		msleep(40)
	set_servo_position(port,end_pos)

            
def arm_ready(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_R, step)
	move_servo_slow(WRIST_PORT, get_servo_position(WRIST_PORT), WRIST_RR, step)
        
def arm_up(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_U, step)
	move_servo_slow(WRIST_PORT, get_servo_position(WRIST_PORT), WRIST_UU, step)
    
def arm_down(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_D, step)
	move_servo_slow(WRIST_PORT, get_servo_position(WRIST_PORT), WRIST_DD, step)
    
def arm_start(step):
	move_servo_slow(ARM_PORT, get_servo_position(ARM_PORT), ARM_S, step)
	move_servo_slow(WRIST_PORT, get_servo_position(WRIST_PORT), WRIST_SS, step)
          
