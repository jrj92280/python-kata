from poker.texas_holdem.score_hand import score_hand


def test_high_card():
    player_one_hand = [['H14', 'C12', 'S11', 'D10', 'S6'], [], [], [], [], [], []]
    player_two_hand = [['H13', 'C12', 'S11', 'D10', 'S6'], [], [], [], [], [], []]

    assert 1 == score_hand(player_one_hand, player_two_hand)
    assert -1 == score_hand(player_two_hand, player_one_hand)
    assert 0 == score_hand(player_one_hand, player_one_hand)


def test_pair():
    player_one_hand = [['H13', 'C12', 'S12', 'D10', 'S6'], [['C12', 'S12']], [], [], [], [], []]
    player_two_hand = [['H14', 'C12', 'S11', 'D10', 'S6'], [], [], [], [], [], []]

    assert 1 == score_hand(player_one_hand, player_two_hand)
    assert -1 == score_hand(player_two_hand, player_one_hand)
    assert 0 == score_hand(player_one_hand, player_one_hand)


def test_pair():
    player_one_hand = [[], [['C12', 'S12']], [], [], [], [], []]
    player_two_hand = [[], [['S2', 'C2'], ['S3', 'C3']], [], [], [], [], []]

    assert 1 == score_hand(player_one_hand, player_two_hand)
    assert -1 == score_hand(player_two_hand, player_one_hand)
    assert 0 == score_hand(player_one_hand, player_one_hand)
