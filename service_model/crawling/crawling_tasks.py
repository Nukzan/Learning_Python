



from background_task import background
import time
@background(schedule = 2)   # per second
def task_hello():
    time_tuple = time.localtime()
    time_str = time.strftime('%m/%d/%Y, %H:%M:%S', time_tuple)
    print('this is test task -> Hello, World!', time_str)
