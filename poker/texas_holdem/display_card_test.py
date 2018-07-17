from poker.texas_holdem.display_card import display_card


def test_face_card_heart():
    expected = '2♥'
    card = display_card('H2')
    assert expected == card


def test_face_card_club():
    expected = '2♣
    card = display_card('C2')
    assert expected == card
#
# def test_face_card_spade():
#     expected = '2♠'
#     card = display_card('S2')
#     assert expected == card
#
# def test_face_card_diamonds():
#     expected = '2♦'
#     card = display_card('D2')
#     assert expected == card
#
# def test_jack_of_diamonds():
#     expected = 'J♦'
#     card = display_card('D11')
#     assert expected == card
