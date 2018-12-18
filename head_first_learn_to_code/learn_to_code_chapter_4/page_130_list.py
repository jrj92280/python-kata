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


# ///////////The Thing-A-Ma-Jig//////////////// page 133
#
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

scores = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]
i = 0
length = len(scores)
while i < length:
    bubble_string = 'Bubble solution #' + str(i)
    print(bubble_string, 'score:', scores[i])
    i = i + 1