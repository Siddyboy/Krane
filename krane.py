#!/usr/bin/env python2.7
# TODO(SCJK): Find out if should be /usr/bin/python2 as detailed in python
# styleguide.
# This code uses WiringPi for Python which uses hardware PWM on Gertboard.
# All print statements in this prog must now be in python 3 format.

from __future__ import print_function   # Allows Python3 style print()            
import wiringpi
import sys
from time import sleep
import pygame
import pygame.locals as CRANE_GLOBALS   # Import this for keyboard K_constants.
import pygame.event as CRANE_EVENTS     # Import this for keyboard event
                                        # detection.
import krane_parts

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
    if __debug__: print("Quiting WiringPi.")
    wiringpi.pwmWrite(18, 0)                # set pwm to zero
    wiringpi.digitalWrite(18, 0)            # port 18 off
    wiringpi.digitalWrite(17, 0)            # port 17 off
    wiringpi.pinMode(17, 0)                 # port 17 back to input mode
    wiringpi.pinMode(18, 0)                 # port 18 back to input mode
    if __debug__: print("Quiting Pygame.")
    pygame.quit()
    if __debug__: print("Raising SystemExit.")
    raise SystemExit
    

def main():

    windowSize = width, height = 500, 400

    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode(windowSize, pygame.RESIZABLE)
    pygame.display.set_caption('Kingsley Krane')

    crane_on = False
    hook_up_slow = False
    hook_down_slow = False
    hook_speed = 0
    
    start_screen = pygame.image.load("assets/cmax.jpg")
    end_screen = pygame.image.load("assets/over.jpg")
    on_button = pygame.image.load("assets/on.jpg")
    off_button = pygame.image.load("assets/off.jpg")

    surface.blit(start_screen, (0, 0))
    pygame.display.update()
        
    try:
        
        hook = krane_parts.krane_hook.KraneHook()	

        while True:

            if crane_on:

                surface.blit(on_button, (0, 0))

                if hook_up_slow is True:
                    hook.up_slow(hook_speed)
                elif hook_down_slow is True:
                    hook.down_slow(hook_speed)
                else:
                    hook.stop()
                     
            elif not crane_on:
                surface.blit(off_button, (0, 0))
            
# Handle user events
            for event in CRANE_EVENTS.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        print("ESC Press Detected")
                        safe_exit()
                    
                    if event.key == pygame.K_UP:
                        print("UP Press Detected")
                        hook_up_slow = True
                        hook_down_slow = False
                    
                    if event.key == pygame.K_DOWN:
                        print("DOWN Press Detected")
                        hook_up_slow = False
                        hook_down_slow = True
                    
                    if event.key == pygame.K_o:
                        print("'O' Press Detected")
                        if not crane_on:o
                            crane_on = True
                        elif crane_on:
                            crane_on = False
 
                elif event.type == pygame.KEYUP:
    
                    if event.key == pygame.K_UP:
                        print("UP Release Detected")
                        hook_up_slow = False
                        hook_down_slow = False
                        
                    if event.key == pygame.K_DOWN:
                        print("DOWN Release Detected")
                        hook_up_slow = False
                        hook_down_slow = False

                elif event.type == CRANE_GLOBALS.QUIT:
                    safe_exit()
                    
            print("Krane On, Hook Up, Hook Down")
            print(crane_on, "   ", hook_up_slow, "  ", hook_down_slow)            
            clock.tick(10)
            pygame.display.update()

    except KeyboardInterrupt:           # trap a CTRL+C keyboard interrupt
        safe_exit()                     # reset ports on interrupt 

    surface.blit(end_screen, (0, 0))
    pygame.display.update()
    safe_exit()                         # reset ports on normal exit

if __name__ == '__main__':
    main()
