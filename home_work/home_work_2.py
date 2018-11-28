import random



def largest(i_list):
    s_list = sorted(i_list)
    largest = s_list[-1]
    return largest


#
# my_list = (1, 6, 35)
# assert 35 == largest(my_list)

r_list = []
for _ in range(5):
    number = random.randint(1, 100)
    r_list.append(number)

assert 5 == len(r_list)
print(r_list)
print(largest(r_list))

# def largest(l_list):
#     for x in range(5):
#         random.randint(1, 101)
#         sorted()
#         return print(l_list)

largest