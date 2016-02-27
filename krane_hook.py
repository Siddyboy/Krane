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
# 
def main()
    
    
    class KraneHook(object):
    
        def stop():
            pass
            
        def up_slow(hook_speed):
            pass
            
        def down_slow(hook_speed):
            pass

if __name__ == "__main__":
    main()

