import wiringpi as wp
from constants import PWM_PIN
from constants import DIR_PIN

class KraneHook(object):
    '''Represents the crane hook itself'''

    def __init__(self):
        '''Stops the hook.'''
        
        self.stop()    
    
    def stop(self):
        '''Stops the hook dead.'''

        wp.digitalWrite(DIR_PIN, 0) 
        wp.pwmWrite(PWM_PIN, 0)
                
    def up_slow(self):
        '''Moves the hook up slowly.'''

        wp.digitalWrite(DIR_PIN, 1)
        wp.pwmWrite(PWM_PIN, 1024)
            
    def down_slow(self):
        '''Moves the hook down slowly.'''

        wp.digitalWrite(DIR_PIN, 0)
        wp.pwmWrite(PWM_PIN, 1023)




