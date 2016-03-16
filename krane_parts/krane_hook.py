import wiringpi

class KraneHook(object):
    '''Represents the crane hook itself'''

    def __init__(self):
        '''Stops the hook.'''
        
        self.stop()    
    
    def stop(self):
        '''Stops the hook dead.'''
	
        wiringpi.pwmWrite(18, 0)
        print("STOP DEAD!")

         
    def up_slow(self, hook_speed):
        '''Moves the hook up slowly.'''
	
        print("Going up slow...")    
        wiringpi.digitalWrite(17, 0)
        wiringpi.pwmWrite(18, 500)
            
    def down_slow(self, hook_speed):
        '''Moves the hook down slowly.'''

        print("Going down slow...")
        wiringpi.digitalWrite(17, 1)
        wiringpi.pwmWrite(18, 500)



