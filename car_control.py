#!/home/pi/server
# coding=utf-8

import  RPi.GPIO as GPIO
import time

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)
L_Motor= GPIO.PWM(PWMA,100)
L_Motor.start(0)
R_Motor = GPIO.PWM(PWMB,100)
R_Motor.start(0)

def t_up(speedL,speedR):                
        L_Motor.ChangeDutyCycle(speedL)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1

        R_Motor.ChangeDutyCycle(speedR)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1       

def t_stop(t_time):
        L_Motor.ChangeDutyCycle(0)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(0)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)

def t_down(speedL,speedR):
        L_Motor.ChangeDutyCycle(speedL)
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(speedR)
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1

def t_left(speedL,speedR):
        L_Motor.ChangeDutyCycle(speedL)
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(speedR)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1

def t_right(speedL,speedR):
        L_Motor.ChangeDutyCycle(speedL)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1

        R_Motor.ChangeDutyCycle(speedR)
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1



