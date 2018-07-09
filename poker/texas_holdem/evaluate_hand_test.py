from poker.texas_holdem.evaluate_hand import evaluate_hand


def test_hand_has_7_cards():
    hand = ['14,A,spades', '14,A,clubs', '14,A,hearts', '14,A,diamonds', '2,2,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert 5 == len(current_hand[0])


def test_high_cards():
    exected_hand = ['14,A,clubs', '14,A,diamonds', '14,A,hearts', '14,A,spades', '4,4,spades']

    hand = ['14,A,spades', '14,A,clubs', '14,A,hearts', '14,A,diamonds', '2,2,spades', '3,3,hearts', '4,4,spades']
    current_hand = evaluate_hand(hand)

    _exected_hand = set(exected_hand)
    _current_hand = set(current_hand[0])

    assert _exected_hand == _current_hand


def test_high_cards_two():
    exected_hand = [['13,K,hearts', '12,Q,clubs', '11,J,spades', '10,10,diamonds', '6,6,spades'], [], [], [], []]

    hand = ['11,J,spades', '12,Q,clubs', '13,K,hearts', '10,10,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert exected_hand == current_hand


def test_one_pair():
    exected_hand = (
    ['13,K,hearts', '13,K,clubs', '11,J,spades', '10,10,diamonds', '6,6,spades'], [['13,K,hearts', '13,K,clubs']])

    hand = ['11,J,spades', '13,K,hearts', '13,K,clubs', '10,10,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    _exected_hand = set(exected_hand[0])
    _current_hand = set(current_hand[0])

    assert _exected_hand == _current_hand
    assert exected_hand[1] == current_hand[1]


def test_one_three_of_kind():
    exected_hand = [['13,K,hearts', '13,K,clubs', '13,K,spades']]

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '10,10,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert exected_hand == current_hand[2]


def test_four_of_kind():
    exected_hand = [['13,K,hearts', '13,K,clubs', '13,K,spades', '13,K,diamonds']]

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '13,K,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert exected_hand == current_hand[3]


def test_full_house():
    exected_hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '6,6,diamonds', '6,6,spades']

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '6,6,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert exected_hand == current_hand[4]


def test_full_house_with_two_pairs():
    exected_hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '6,6,diamonds', '6,6,spades']

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '4,4,hearts', '4,4,spades', '6,6,diamonds', '6,6,spades']

    current_hand = evaluate_hand(hand)

    assert exected_hand == current_hand[4]
