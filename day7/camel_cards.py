
CARD_VALUES = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

JOKER_CARD_VALUES = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}


def process_hands(filename):
    hands = []

    with open(filename) as hand_lines:
        for hand in hand_lines:
            hand = hand.split()
            hands.append([hand[0], int(hand[1])])

    return hands


def sort_pile_original(e):
    card_num = 0
    i = len(e[0])
    for card in e[0]:
        mult = int(str(1) + str(0)*(i*2))
        card_num += CARD_VALUES[card] * mult
        i -= 1
    return card_num


def sort_pile_joker(e):
    card_num = 0
    i = len(e[0])
    for card in e[0]:
        mult = int(str(1) + str(0)*(i*2))
        card_num += JOKER_CARD_VALUES[card] * mult
        i -= 1
    return card_num


def calc_pile_values(i, pile):
    pile_total = 0
    for hand in pile:
        pile_total += hand[1] * i
        i += 1
    return pile_total


def calculate_joker_winnings(filename):
    five_of_a_kind = []
    four_of_a_kind = []
    full_houses = []
    three_of_a_kind = []
    two_pairs = []
    one_pairs = []
    high_cards = []

    hand_data = process_hands(filename)

    for hand in hand_data:
        hand_set = list(set(hand[0]))
        if len(hand_set) == 1:
            five_of_a_kind.append(hand)
        elif len(hand_set) == 2:
            value_count = hand[0].count(hand_set[0])
            if 'J' in hand_set:
                five_of_a_kind.append(hand)
            elif value_count == 1 or value_count == 4:
                four_of_a_kind.append(hand)
            else:
                full_houses.append(hand)
        elif len(hand_set) == 3:
            value_count_one, value_count_two, value_count_three = hand[0].count(hand_set[0]), hand[0].count(hand_set[1]), hand[0].count(hand_set[2])
            if 'J' in hand_set:
                if hand[0].count('J') != 1:
                    four_of_a_kind.append(hand)
                elif value_count_one == 3 or value_count_two == 3 or value_count_three == 3:
                    four_of_a_kind.append(hand)
                else:
                    full_houses.append(hand)
            elif value_count_one == 3 or value_count_two == 3 or value_count_three == 3:
                three_of_a_kind.append(hand)
            else:
                two_pairs.append(hand)
        elif len(hand_set) == 4:
            if 'J' in hand_set:
                three_of_a_kind.append(hand)
            else:
                one_pairs.append(hand)
        else:
            if 'J' in hand[0]:
                one_pairs.append(hand)
            else:
                high_cards.append(hand)

    high_cards.sort(key=sort_pile_joker)
    five_of_a_kind.sort(key=sort_pile_joker)
    four_of_a_kind.sort(key=sort_pile_joker)
    full_houses.sort(key=sort_pile_joker)
    three_of_a_kind.sort(key=sort_pile_joker)
    two_pairs.sort(key=sort_pile_joker)
    one_pairs.sort(key=sort_pile_joker)

    i = 1
    winnings = calc_pile_values(i, high_cards)
    i += len(high_cards)
    winnings += calc_pile_values(i, one_pairs)
    i += len(one_pairs)
    winnings += calc_pile_values(i, two_pairs)
    i += len(two_pairs)
    winnings += calc_pile_values(i, three_of_a_kind)
    i += len(three_of_a_kind)
    winnings += calc_pile_values(i, full_houses)
    i += len(full_houses)
    winnings += calc_pile_values(i, four_of_a_kind)
    i += len(four_of_a_kind)
    winnings += calc_pile_values(i, five_of_a_kind)

    return winnings


def calculate_winnings(filename):
    five_of_a_kind = []
    four_of_a_kind = []
    full_houses = []
    three_of_a_kind = []
    two_pairs = []
    one_pairs = []
    high_cards = []

    hand_data = process_hands(filename)

    for hand in hand_data:
        hand_set = list(set(hand[0]))
        if len(hand_set) == 1:
            five_of_a_kind.append(hand)
        elif len(hand_set) == 2:
            value_count = hand[0].count(hand_set[0])
            if value_count == 1 or value_count == 4:
                four_of_a_kind.append(hand)
            else:
                full_houses.append(hand)
        elif len(hand_set) == 3:
            value_count_one, value_count_two, value_count_three = hand[0].count(hand_set[0]), hand[0].count(hand_set[1]), hand[0].count(hand_set[2])
            if value_count_one == 3 or value_count_two == 3 or value_count_three == 3:
                three_of_a_kind.append(hand)
            else:
                two_pairs.append(hand)
        elif len(hand_set) == 4:
            one_pairs.append(hand)
        else:
            high_cards.append(hand)

    high_cards.sort(key=sort_pile_original)
    five_of_a_kind.sort(key=sort_pile_original)
    four_of_a_kind.sort(key=sort_pile_original)
    full_houses.sort(key=sort_pile_original)
    three_of_a_kind.sort(key=sort_pile_original)
    two_pairs.sort(key=sort_pile_original)
    one_pairs.sort(key=sort_pile_original)

    i = 1
    winnings = calc_pile_values(i, high_cards)
    i += len(high_cards)
    winnings += calc_pile_values(i, one_pairs)
    i += len(one_pairs)
    winnings += calc_pile_values(i, two_pairs)
    i += len(two_pairs)
    winnings += calc_pile_values(i, three_of_a_kind)
    i += len(three_of_a_kind)
    winnings += calc_pile_values(i, full_houses)
    i += len(full_houses)
    winnings += calc_pile_values(i, four_of_a_kind)
    i += len(four_of_a_kind)
    winnings += calc_pile_values(i, five_of_a_kind)

    return winnings


def main():
    print(calculate_winnings('camel_cards_hand_data.txt'))
    print(calculate_joker_winnings('camel_cards_hand_data.txt'))


if __name__ == '__main__':
    main()
