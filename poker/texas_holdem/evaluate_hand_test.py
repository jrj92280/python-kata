from poker.texas_holdem.evaluate_hand import evaluate_hand


def test_hand_has_7_cards():
    hand = ['14,A,spades', '14,A,clubs', '14,A,hearts', '14,A,diamonds', '2,2,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert 5 == len(current_hand[0])


def test_high_cards():
    expected_hand = ['14,A,clubs', '14,A,diamonds', '14,A,hearts', '14,A,spades', '4,4,spades']

    hand = ['14,A,spades', '14,A,clubs', '14,A,hearts', '14,A,diamonds', '2,2,spades', '3,3,hearts', '4,4,spades']
    current_hand = evaluate_hand(hand)

    _expected_hand = set(expected_hand)
    _current_hand = set(current_hand[0])

    assert _expected_hand == _current_hand


def test_high_cards_two():
    expected_hand = [['13,K,hearts', '12,Q,clubs', '11,J,spades', '10,10,diamonds', '6,6,spades'], [], [], [], [], [],
                     []]

    hand = ['11,J,spades', '12,Q,clubs', '13,K,hearts', '10,10,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand


def test_one_pair():
    expected_hand = (
    ['13,K,hearts', '13,K,clubs', '11,J,spades', '10,10,diamonds', '6,6,spades'], [['13,K,hearts', '13,K,clubs']])

    hand = ['11,J,spades', '13,K,hearts', '13,K,clubs', '10,10,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    _expected_hand = set(expected_hand[0])
    _current_hand = set(current_hand[0])

    assert _expected_hand == _current_hand
    assert expected_hand[1] == current_hand[1]


def test_one_three_of_kind():
    expected_hand = [['13,K,hearts', '13,K,clubs', '13,K,spades']]

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '10,10,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[2]


def test_four_of_kind():
    expected_hand = [['13,K,hearts', '13,K,clubs', '13,K,spades', '13,K,diamonds']]

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '13,K,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[3]


def test_full_house():
    expected_hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '6,6,diamonds', '6,6,spades']

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '6,6,diamonds', '6,6,spades', '3,3,hearts', '4,4,spades']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[4]


def test_full_house_with_two_pairs():
    expected_hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '6,6,diamonds', '6,6,spades']

    hand = ['13,K,hearts', '13,K,clubs', '13,K,spades', '4,4,hearts', '4,4,spades', '6,6,diamonds', '6,6,spades']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[4]


def test_straight():
    expected_hand = ['14,A,hearts', '13,K,hearts', '12,hearts,Q', '11,J,hearts', '10,10,hearts']

    hand = ['13,K,hearts', '14,A,hearts', '12,hearts,Q', '11,J,hearts', '10,10,hearts', '4,4,hearts', '2,2,hearts']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]


def test_straight_with_inner_pair():
    expected_hand = ['14,A,hearts', '13,K,hearts', '12,hearts,Q', '11,J,hearts', '10,10,hearts']

    hand = ['13,K,hearts', '14,A,hearts', '12,hearts,Q', '11,J,hearts', '10,10,hearts', '4,4,hearts', '13,K,clubs']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]


def test_straight_with_7():
    expected_hand = ['14,A,hearts', '13,K,hearts', '12,Q,hearts', '11,J,hearts', '10,10,hearts', '9,9,hearts',
                     '8,8,hearts']

    hand = ['13,K,hearts', '14,A,hearts', '12,Q,hearts', '11,J,hearts', '10,10,hearts', '9,9,hearts', '8,8,hearts']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]


def test_flush():
    expected_hand = ['14,A,hearts', '13,K,hearts', '12,Q,hearts', '11,J,hearts', '10,10,hearts', '9,9,hearts',
                     '2,2,hearts']

    hand = ['13,K,hearts', '14,A,hearts', '12,Q,hearts', '11,J,hearts', '10,10,hearts', '9,9,hearts', '2,2,hearts']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[6]
