# eighties = ['', 'duran duran', 'B-52s', 'muse']
# newwave = ['flock of seagulls', 'postal service']
#
# remember = eighties[1]
#
# eighties[1] = 'culture club'
#
# band = newwave[0]
#
# eighties[3] = band
#
# eighties[0] = eighties[2]
#
# eighties[2] = remember
#
# print(eighties)
#
# length = len(eighties)
# print(length)
# last = eighties[length - 1]
# print(last)
# second_last = eighties[length - 2]
# print(second_last)
# third_last = eighties[length - 3]
# print((third_last))


# ///////////The Thing-A-Ma-Jig//////////////// page 133#
# characters = ['t', 'a', 'c', 'o']
# output = ''
# length = len(characters)
# i = 0
# while i < length:
#     output = output + characters[i]
#     i = i + 1
#
# length = length * -1
# i = -2
#
# while i >= length:
#     output = output + characters[i]
#     i = i - 1
#
# print(output)

# ////////////Bubbles-R-Us///////////// page 135
#
# scores = [60, 50, 60, 58, 54, 54,
#           58, 50, 52, 54, 48, 69,
#           34, 55, 51, 52, 44, 51,
#           69, 64, 66, 55, 52, 61,
#           46, 31, 57, 52, 44, 18,
#           41, 53, 55, 61, 51, 44]
#
# high_score = 0
#
# high_score_indexes = []
# length = len(scores)
#
# for i in range(length):
#     print('Bubble_solution #' + str(i), 'score:', scores[i])
#
#     if scores[i] >= high_score:
#         if high_score != scores[i]:
#             high_score_indexes = []
#
#         high_score = scores[i]
#         high_score_indexes.append(i)
#
#         print('Bubbles test:', length)
#         print('Highest bubble score:', high_score)
#
#         print('Solution index with highest score:', i)
#
# print('!!!!!! ', high_score_indexes)
# ///////////smoothies//////////  page 142

#
# smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
# length = len(smoothies)
# for i in range(length):
#     output = 'We serve ' , i, smoothies[i]
#     print(output)

# //////// page 150 //////////
# import random
#
# smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
#
# # manual random.choice
# print("--- manual random")
# random_flav = smoothies[random.randint(0, len(smoothies) - 1)]
# print(random_flav)
#
# # random.choice
# print("--- random choice")
# print(random.choice(smoothies))
#
# print("--- smoothie combos!")
# smoothie_choice = [0, 2] # manually picked combo -- customer order
#
# smoothie = '-'.join([smoothies[x] for x in smoothie_choice])
# print(smoothie)
#
# if 'coconut' in smoothie:
#     print('Yum')

# import random
# [random.randint(0,1) for x in range(5)] #  random has coconut
#
# combined_smoothies = []
# i = 0
# while i < 5:
#     combos = random.randint(1,3)
#     smoothie_combo = "-".join([random.choice(smoothies) for _ in range(combos)])
#     print(smoothie_combo)
#     combined_smoothies.append(smoothie_combo)
#     i = i + 1
#
# print(combined_smoothies)
# //// page 156 ////
mystery = ['secret'] * 5
print(mystery)
mystery = ' secret' * 5
print(mystery)
