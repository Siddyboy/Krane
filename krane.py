#!/usr/bin/env python2.7
# This code uses WiringPi for Python which uses hardware PWM on Gertboard.
# All print statements in this prog must now be in python 3 format.
# 

# General Imports
from __future__ import print_function               
import wiringpi
import sys
from time import sleep

# Pygame Imports
import pygame
import pygame.locals as CRANE_GLOBALS       # Import this for keyboard K_ constants.
import pygame.event as CRANE_EVENTS         # Import this for keyboard event detection.

debug = True

windowSize = width, height = 500, 400

pygame.init()
surface = pygame.display.set_mode(windowSize, pygame.RESIZABLE)
pygame.display.set_caption('Kingsley Krane')

wiringpi.wiringPiSetupGpio()                # Initialise wiringpi GPIO
wiringpi.pinMode(18,2)                      # Set up GPIO 18 to PWM mode
wiringpi.pinMode(17,1)                      # GPIO 17 to output
wiringpi.digitalWrite(17, 0)                # port 17 off for rotation one way
wiringpi.pwmWrite(18,0)                     # set pwm to zero initially

craneStarted = False
craneStopped = False
upSlow = False
downSlow = False
stopNow = True

# Funtion to handle a safe exit.
def safeExit():
    if debug:
        print("Quiting WiringPi.")
    wiringpi.pwmWrite(18,0)                 # set pwm to zero
    wiringpi.digitalWrite(18, 0)            # port 18 off
    wiringpi.digitalWrite(17, 0)            # port 17 off
    wiringpi.pinMode(17,0)                  # port 17 back to input mode
    wiringpi.pinMode(18,0)                  # port 18 back to input mode
    if debug:
        print("Quiting Pygame.")
    pygame.quit()
    if debug:
        print("Raising SystemExit.")
    raise SystemExit
    print("Bye 3")

# define the main loop that we run in four different ways 
# controlled by the function arguments
def loop(start_pwm, stop_pwm, step, printchar): 
    for x in range(start_pwm, stop_pwm, step):  
        wiringpi.pwmWrite(18,x)
        # if x is an exact multiple of 19, i.e. x/19 has remainder 0
        if x % (19) == 0:                   
            display(printchar)              # print the + or - character
        sleep(rest)

rest = 0.013                    # vary "sleep" time for testing purposes
                                #~ 0.013 is about right in use
# Main loop
try:
    while True:
        if craneStarted and not craneStopped:

            print("Krane Started")
            sleep(5)
            
            if upSlow is True:
                #hook.upSlow()
                print("up slow called")

            if downSlow is True:
                #hook.downSlow()
                print("down slow called")

            if stopNow is True:
                #hook.stop()
                #everything else stop too.
                print("Emergency Stop!")

        elif not craneStarted and not craneStopped:
            print("Start Screen Displayed! Welcome to Crane")

        elif craneStarted and craneStopped:
            print("End Screen Displayed. Bye!")

        # Handle user events
        for event in CRANE_EVENTS.get():

            print("inside event for")

            if event.type == pygame.KEYDOWN:

                print("inside event if")

                if event.key == pygame.K_ESCAPE:
                    safeExit()
                elif event.key == pygame.K_UP:
                    upSlow = True
                    downSlow = False
                elif event.key == pygame.K_DOWN:
                    upSlow = False
                    downSlow = True
                elif event.key == pygame.K_s:
                    upSlow = False
                    downSlow = False
                    stopNow = True
                elif event.key == pygame.K_o:
                    if not craneStarted and not craneStopped:
                        craneStarted = True
                    elif craneStarted and not craneStopped:
                        craneStopped = True

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    upSlow = False
                if event.key == pygame.K_DOWN:
                    downSlow = False

            if event.type == CRANE_GLOBALS.QUIT:
                safeExit()       

except KeyboardInterrupt:           # trap a CTRL+C keyboard interrupt
    safeExit()                      # reset ports on interrupt 

safeExit()                          # reset ports on normal exit


            
            


#try:
#                                    # the arguments for loop are marts hidden change 
#    loop(140, 1024, 1, '+')         #(start_pwm, stop_pwm, step, printchar)
#    loop(994, 110, -1, '-')         # 140 is enough to spin up my motor,
#                                    # 70 is about right to stop it
#
#    wiringpi.digitalWrite(17, 1)    # port 17 ON for opposite rotation
#  
#    loop(954, 89, -1, '+')
#    loop(121, 1024, 1, '-')
#

