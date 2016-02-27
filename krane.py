#!/usr/bin/env python2.7
# TODO(SCJK): Find out if should be /usr/bin/python2 as detailed in python
# styleguide.
# This code uses WiringPi for Python which uses hardware PWM on Gertboard.
# All print statements in this prog must now be in python 3 format.
# Sids Test Change.
# Another thing to delete
# Sids Test Change 2.
# Sids Test Change 3 at work.
# Another change from work

from __future__ import print_function               
import wiringpi
import sys
from time import sleep
import pygame
import pygame.locals as CRANE_GLOBALS   # Import this for keyboard K_constants.
import pygame.event as CRANE_EVENTS     # Import this for keyboard event
                                        # detection.



def safe_exit():
    """Ensures exit is handled cleanly.
    
    Shuts down hardware, quits pygame, and raises SystemExit.
    
    Args:
        None.
    
    Returns:
        None.
    
    Raises:
        SystemExit.
    """
    if __debug__:
        print("Quiting WiringPi.")
    wiringpi.pwmWrite(18,0)                 # set pwm to zero
    wiringpi.digitalWrite(18, 0)            # port 18 off
    wiringpi.digitalWrite(17, 0)            # port 17 off
    wiringpi.pinMode(17,0)                  # port 17 back to input mode
    wiringpi.pinMode(18,0)                  # port 18 back to input mode
    if __debug__:
        print("Quiting Pygame.")
    pygame.quit()
    if __debug__:
        print("Raising SystemExit.")
    raise SystemExit
    print("Bye 3")

# TODO(SCJK): Abstract this functionality away into a class in another module.
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

                                
def main():

    windowSize = width, height = 500, 400

    pygame.init()
    surface = pygame.display.set_mode(windowSize, pygame.RESIZABLE)
    pygame.display.set_caption('Kingsley Krane')

    wiringpi.wiringPiSetupGpio()                # Initialise wiringpi GPIO
    wiringpi.pinMode(18,2)                      # Set up GPIO 18 to PWM mode
    wiringpi.pinMode(17,1)                      # GPIO 17 to output
    wiringpi.digitalWrite(17, 0)                # port 17 off for rotation one way
    wiringpi.pwmWrite(18,0)                     # set pwm to zero initially

    crane_started = False
    crane_stopped = False
    up_slow = False
    down_slow = False
    stop_now = True
    hook_speed = 0
    
    try:
        while True:
            if crane_started and not crane_stopped:

                print("Krane Started")
                sleep(5)
            
                if up_slow is True:
                    # TODO(SCJK): hook.upSlow(hookSpeed?)
                    print("up slow called")

                if down_slow is True:
                    # TODO(SCJK): hook.downSlow()
                    print("down slow called")

                if stop_now is True:
                    # TODO(SCJK): hook.stop()
                    # TODO(SCJK): everything else stop too.
                    print("Emergency Stop!")

            elif not crane_started and not crane_stopped:
                print("Start Screen Displayed! Welcome to Crane")

            elif crane_started and crane_stopped:
                print("End Screen Displayed. Bye!")

            # Handle user events
            for event in CRANE_EVENTS.get():

                print("inside event for")

                if event.type == pygame.KEYDOWN:

                    print("inside event if")

                    if event.key == pygame.K_ESCAPE:
                        safe_exit()
                    elif event.key == pygame.K_UP:
                        up_slow = True
                        down_slow = False
                    elif event.key == pygame.K_DOWN:
                        up_slow = False
                        down_slow = True
                    elif event.key == pygame.K_s:
                        up_slow = False
                        down_slow = False
                        stop_now = True
                    elif event.key == pygame.K_o:
                        if not crane_started and not crane_stopped:
                            crane_started = True
                        elif crane_started and not crane_stopped:
                            crane_stopped = True

                if event.type == pygame.KEYUP:
    
                    if event.key == pygame.K_UP:
                        up_slow = False
                    if event.key == pygame.K_DOWN:
                        down_slow = False

                if event.type == CRANE_GLOBALS.QUIT:
                    safe_exit()       

    except KeyboardInterrupt:           # trap a CTRL+C keyboard interrupt
        safe_exit()                     # reset ports on interrupt 

    safe_exit()                          # reset ports on normal exit

if __name__ == '__main__':
    main()
            
# TODO(SCJK): Cruft left over from original GertBoard example. Delete when up
# and running with crane. Also contains Martin's hidden change!
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
