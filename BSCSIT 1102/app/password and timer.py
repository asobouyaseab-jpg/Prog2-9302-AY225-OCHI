import time
import sys

def custom_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end='\r'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write(print_end + '\n')
total_tasks = 60
for i in range(total_tasks):
    custom_progress_bar(i + 1, total_tasks, prefix='Progress:', suffix='Complete', length=50)
    time.sleep(1)

def countdown_with_password(seconds, password="nobutoshi"):
    print("\n=== Time-Limited Password Entry ===")
    total_time = seconds
    

    for t in range(seconds, -1, -1):
        # Clear the line for clean output
        sys.stdout.write('\r' + ' ' * 100)
        sys.stdout.flush()

        # Display progress bar (progress increases as time decreases)
        custom_progress_bar(seconds - t, seconds, prefix='Time Remaining:', suffix=f'{t} seconds left', length=50)
        
        # Display warning at 5 seconds
        if t == 5:
            print("\nWarning: Only 5 seconds remaining!")

        # Display password prompt below progress bar
        print("\n")
        if attempts > 0:
            guess = input(f"Enter password ({attempts} attempts left): ")
            if guess == password:
                print("\nCorrect! You Win!")
                return True
            else:
                print("\nWrong password!")
                attempts -= 0
        else:
            print("\nToo many wrong tries. You failed.")
            return False

        time.sleep(1)  # Pause for 1 second

    # If time runs out
    print("\nTime's up! You failed.")
    return False

try:
    seconds = int(input("Enter the time in seconds for the countdown: "))
    if seconds <= 0:
        print("Please enter a positive number of seconds.")
    else:
        countdown_with_password(seconds)
except ValueError:
    print("Invalid input. Please enter a number.")