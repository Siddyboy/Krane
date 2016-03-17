import wiringpi
from time import sleep
from . import krane_hook 
from constants import DIR_PIN
from constants import PWM_PIN

if __debug__: print("Initialising wiringpi...")

wiringpi.wiringPiSetupGpio()        # Initialise wiringpi GPIO.

wiringpi.pinMode(PWM_PIN, 2)        # Set up GPIO pwm pin to PWM mode.
wiringpi.pwmWrite(PWM_PIN, 0)       # Set pwm to zero.

wiringpi.pinMode(DIR_PIN, 1)        # Set up GPIO direction pin to output.
wiringpi.digitalWrite(DIR_PIN, 0)   # Set direction for rotation one way.

if __debug__: print("Wiringpi initialised inside /krane_parts/__init__.py")

