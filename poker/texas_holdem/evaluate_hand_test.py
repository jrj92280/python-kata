from poker.texas_holdem.evaluate_hand import evaluate_hand


def test_hand_has_7_cards():
    hand = ['S14', 'C14', 'H14', 'D14', 'S2', 'H3', 'S4']

    current_hand = evaluate_hand(hand)

    assert 5 == len(current_hand[0])


def test_high_cards():
    expected_hand = ['C14', 'D14', 'H14', 'S14', 'S4']

    hand = ['S14', 'C14', 'H14', 'D14', 'S2', 'H3', 'S4']
    current_hand = evaluate_hand(hand)

    _expected_hand = set(expected_hand)
    _current_hand = set(current_hand[0])

    assert _expected_hand == _current_hand


def test_high_cards_two():
    expected_hand = [['H13', 'C12', 'S11', 'D10', 'S6'], [], [], [], [], [], []]

    hand = ['S11', 'C12', 'H13', 'D10', 'S6', 'H3', 'S4']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand


def test_one_pair():
    expected_hand = (
        ['H13', 'C13', 'S11', 'D10', 'S6'], [['H13', 'C13']])

    hand = ['S11', 'H13', 'C13', 'D10', 'S6', 'H3', 'S4']

    current_hand = evaluate_hand(hand)

    _expected_hand = set(expected_hand[0])
    _current_hand = set(current_hand[0])

    assert _expected_hand == _current_hand
    assert expected_hand[1] == current_hand[1]


def test_one_three_of_kind():
    expected_hand = [['H13', 'C13', 'S13']]

    hand = ['H13', 'C13', 'S13', 'D10', 'S6', 'H3', 'S4']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[2]


def test_four_of_kind():
    expected_hand = [['H13', 'C13', 'S13', 'D13']]

    hand = ['H13', 'C13', 'S13', 'D13', 'S6', 'H3', 'S4']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[3]


def test_full_house():
    expected_hand = ['H13', 'C13', 'S13', 'D6', 'S6']

    hand = ['H13', 'C13', 'S13', 'D6', 'S6', 'H3', 'S4']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[4]


def test_full_house_with_two_pairs():
    expected_hand = ['H13', 'C13', 'S13', 'D6', 'S6']

    hand = ['H13', 'C13', 'S13', 'H4', 'S4', 'D6', 'S6']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[4]


def test_straight():
    expected_hand = ['H14', 'H13', 'H12', 'H11', 'H10']

    hand = ['H13', 'H14', 'H12', 'H11', 'H10', 'H4', 'H2']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]


def test_straight_with_inner_pair():
    expected_hand = ['H14', 'H13', 'H12', 'H11', 'H10']

    hand = ['H13', 'H14', 'H12', 'H11', 'H10', 'H4', 'C13']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]


def test_straight_with_7():
    expected_hand = ['H14', 'H13', 'H12', 'H11', 'H10', 'H9', 'H8']

    hand = ['H13', 'H14', 'H12', 'H11', 'H10', 'H9', 'H8']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]


def test_flush():
    expected_hand = ['H14', 'H13', 'H12', 'H11', 'H10', 'H9', 'H2']

    hand = ['H13', 'H14', 'H12', 'H11', 'H10', 'H9', 'H2']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[6]


def test_ace_low_straight():
    expected_hand = ['H5', 'H4', 'H3', 'H2', 'H14']

    hand = ['C8', 'S9', 'H14', 'H2', 'H3', 'H4', 'H5']

    current_hand = evaluate_hand(hand)

    assert expected_hand == current_hand[5]
