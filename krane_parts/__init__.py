#Do wiringpi inits in here now.
import wiringpi
from time import sleep
from . import krane_hook 

if __debug__: print("Initialising wiringpi...")
wiringpi.wiringPiSetupGpio()	# Initialise wiringpi GPIO
wiringpi.pinMode(18,2)          # Set up GPIO 18 to PWM mode
wiringpi.pinMode(17,1)          # GPIO 17 to output
wiringpi.digitalWrite(17, 0)    # Port 17 off for rotation one way
wiringpi.pwmWrite(18,0)         # Set pwm to zero initially
if __debug__: print("Wiringpi initialised inside /krane_parts/__init__.py")
sleep(5)

