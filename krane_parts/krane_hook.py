import wiringpi
from constants import PWM_PIN
from constants import DIR_PIN

class KraneHook(object):
    '''Represents the crane hook itself'''

    def __init__(self):
        '''Stops the hook.'''
        
        self.stop()    
    
    def stop(self):
        '''Stops the hook dead.'''
	
        wiringpi.pwmWrite(PWM_PIN, 0)
        print("STOP DEAD!")
         
    def up_slow(self, hook_speed):
        '''Moves the hook up slowly.'''
	
        print("Going up slow...")    
        wiringpi.digitalWrite(DIR_PIN, 0)
        wiringpi.pwmWrite(PWM_PIN, 600)
            
    def down_slow(self, hook_speed):
        '''Moves the hook down slowly.'''

        print("Going down slow...")
        #wiringpi.digitalWrite(DIR_PIN, 1)
        #wiringpi.pwmWrite(PWM_PIN, 500)
        wiringpi.digitalWrite(DIR_PIN, 1)
        wiringpi.pwmWrite(PWM_PIN, 1024)



