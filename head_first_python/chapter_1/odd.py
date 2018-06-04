from datetime import datetime

import random
import time



odds = [number for number in range(1, 60, 2 )]
print(odds)
right_this_minute = datetime.today().minute
print(right_this_minute)


for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("odd ball")
    elif right_this_minute==6:
        print("happy soul")
    else:
        print("even steven")
    wait_time = random.randint(1, 60)
    time.sleep(wait_time)