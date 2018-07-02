import random

player_count = int(input("How many players? "))

player_names = []


for player in range(player_count):
    player_name = input('name:')
    player_names.append([player_name, []])

deck = ['A, spades', 'A, clubs', 'A, hearts', 'A, dimonds',
         'K, spades', 'K, clubs', 'K, hearts', 'K, dimonds',
         'Q, spades', 'Q, clubs', 'Q, hearts', 'Q, dimonds',
         'J, spades', 'J, clubs', 'J, hearts', 'J, dimonds',
         '10, spades', '10, clubs', '10, hearts', '10, dimonds',
         '9, spades', '9, clubs', '9, hearts', '9, dimonds',
         '8, spades', '8, clubs', '8, hearts', '8, dimonds',
         '7, spades', '7, clubs', '7, hearts', '7, dimonds',
         '6, spades', '6, clubs', '6, hearts', '6, dimonds',
         '5, spades', '5, clubs', '5, hearts', '5, dimonds',
         '4, spades', '4, clubs', '4, hearts', '4, dimonds',
         '3, spades', '3, clubs', '3, hearts', '3, dimonds',
         '2, spades', '2, clubs', '2, hearts', '2, dimonds']

random.shuffle(deck)

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

# NEXT: burn a card with pop

# NEXT: create list for turned cards

# NEXT: pop three into turned cards

# NEXT: burn card

# NEXT: pop card into turned cards

# NEXT: burn card

# NEXT: pop card into turned cards -- river

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
