
print ("---------99 Bottle of beer on the wall------")
import random


beer_count = random.randint(20, 99)

word = "bottles"

for beer_num in range(beer_count, 0 , -1):
    print(beer_num,word,"of beer on the wall.")
    print("take one down")
    print("pass it around")

    if beer_num == 1:
        print("no more bottles of beer on the wall")
    else:
        new_num = beer_num -1
        if new_num == 1:
            word = "bottle"
        print(str(new_num) + ' ' + word + " of beer on the wall")
