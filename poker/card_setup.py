import random

player_names = []

player_count = 2  # int(input("How many players? "))

# for player in range(player_count):
#     player_name = input('name:')
#     player_names.append([player_name, []])

player_names.append(["jj", []])
player_names.append(["jk", []])

deck = ['14, A, spades', '14, A, clubs', '14, A, hearts', '14, A, dimonds',
        '13, K, spades', '13, K, clubs', '13, K, hearts', '13, K, dimonds',
        '12,Q, spades', '12,Q, clubs', '12,Q, hearts', '12,Q, dimonds',
        '11,J, spades', '11,J, clubs', '11,J, hearts', '11,J, dimonds',
        '10,10, spades', '10,10, clubs', '10,10, hearts', '10,10, dimonds',
        '9,9, spades', '9,9,clubs', '9,9, hearts', '9,9, dimonds',
        '8,8, spades', '8,8, clubs', '8,8, hearts', '8,8, dimonds',
        '7,7, spades', '7,7, clubs', '7,7, hearts', '7,7, dimonds',
        '6,6, spades', '6,6, clubs', '6,6, hearts', '6,6, dimonds',
        '5,5, spades', '5,5, clubs', '5,5, hearts', '5,5, dimonds',
        '4,4, spades', '4,4, clubs', '4,4, hearts', '4,4, dimonds',
        '3,3, spades', '3,3, clubs', '3,3, hearts', '3,3, dimonds',
        '2,2, spades', '2,2, clubs', '2,2, hearts', '2,2, dimonds']

random.shuffle(deck)
for card in deck:
    card_parts = card.split(",")
    print(card_parts[1].strip() + ' of ' + card_parts[2].strip() + ' - ' + card_parts[0].strip())

if "14" in deck:
    print('A')

cards_needed = 2

for _ in range(cards_needed):
    for player in player_names:
        card = deck.pop()
        # ['jj', []]
        player[1].append(card)

# probably dont want this

card = deck.pop()
deck.pop()
# player_name.append[player_name,card]:


for player in player_names:
    print(player[0])
    print(player[1])

burn_card = deck.pop()

card_1 = deck.pop()
card_2 = deck.pop()
card_3 = deck.pop()

flop = [card_1, card_2, card_3]
print(flop)

burn_card_2 = deck.pop()

# flop.append( deck.pop())
flop = flop + [deck.pop()]

print(flop)

burn_card_3 = deck.pop()

flop = flop + [deck.pop()]

print(flop)

# NEXT: SCORE HAND !!! - big task


# IGNORE THIS
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# your_list = [1,2,3,4,5,6,]
# your_list.append(7)
# # assert 7 is not in the list
# is7 = False
# for i in your_list:
#     if i == 7:
#         is7 = True
#
# print (your_list)
# print (is7)
#
# my_list =["s",'t','r','y','q','p']
#
# for i in my_list:
#     if i == 'p':
#         print ('p')
#
#
# my_str = 'gjfslhh'
# for character in my_str:
#     if character == 'p':
#         print ('p')
#
# duplicates = 'aabcdojggnmmvcxzzwdffagjtyrukltilyfjkfu!!ççHHHH'
#
# found_characters ={}
# for d in duplicates:
#     if d not in found_characters:
#         found_characters [d] = 1
#         continue
#     found_characters [d] = found_characters [d] + 1
#
# print (found_characters)
#
# for key, value in found_characters.items():
#     if value == 1:
#         continue
#     print(key, value)
