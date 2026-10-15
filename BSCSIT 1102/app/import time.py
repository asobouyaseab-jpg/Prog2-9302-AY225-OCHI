import time 
def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,end="\r")
        time.sleep(1) # Pause for 1 second
        t -= 1 # Decrement the time
        
    print("Time's up!")        
try:
    seconds = int (input("Enter the time in seconds for the countdown:"))    
    countdown(seconds)
except ValueError:
    print("Invalid input. please enter the number.")
    