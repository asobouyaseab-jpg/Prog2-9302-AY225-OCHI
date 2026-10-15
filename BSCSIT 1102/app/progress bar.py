import time
import sys
def custom_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, 
fill='█', print_end='\r'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write(print_end + '\n')
total_tasks = 100
for i in range(total_tasks):
    custom_progress_bar(i + 1, total_tasks, prefix='Progress:', suffix='Complete', length=50)
    time.sleep(0.05)