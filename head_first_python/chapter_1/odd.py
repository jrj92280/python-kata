from datetime import datetime

odds = [number for number in range(1, 60, 2)]
print(odds)
right_this_minute = datetime.today().minute
print(right_this_minute)
if right_this_minute in odds:
    print("odd ball")
else:
    print("even steven")
