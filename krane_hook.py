# TODO(SCJK): Abstract this functionality away into a class in another module.
# define the main loop that we run in four different ways 
# controlled by the function arguments
#def loop(start_pwm, stop_pwm, step, printchar):
#    for x in range(start_pwm, stop_pwm, step):
#        wiringpi.pwmWrite(18,x)
#        # if x is an exact multiple of 19, i.e. x/19 has remainder 0
#        if x % (19) == 0:
#            display(printchar)              # print the + or - character
#        sleep(rest)
#
#rest = 0.013                    # vary "sleep" time for testing purposes
#                                #~ 0.013 is about right in use
 
class KraneHook(object):
    '''Represents the crane hook itself'''
    pass

#        def __init__(self):
#	    pass

    def stop(self):
        '''Stops the hook dead.'''
        print("STOP DEAD!")

#            hook_speed = 0
#	    return hook_speed
#            
#        def up_slow(self, hook_speed):
#            pass
#            
#        def down_slow(self, hook_speed):
#            pass


