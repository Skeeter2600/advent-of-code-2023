
def scratch_sub_elements(scratch_off_dict, start, won_cards):
    total_cards = 1
    count = 1
    while count <= won_cards:
        numbers = scratch_off_dict[str(start+count)]['numbers']
        win_values = scratch_off_dict[str(start + count)]['win_values']
        card_total = 0
        for number in win_values:
            for value in numbers:
                if value.strip() == number:
                    card_total += 1
        total_cards += scratch_sub_elements(scratch_off_dict, start+count, card_total)
        count += 1

    return total_cards


def get_total_scratchers(filename):
    total_cards = 0
    scratch_off_dict = {}

    with open(filename) as pile:
        for card in pile:
            broken_up = card.split(':')[1].strip().split('|')
            scratch_off_dict[card.split(':')[0].strip().split()[1]] = {'win_values': broken_up[0].split(),
                                                                       'numbers': broken_up[1].split()}
        card_num = 1
        while card_num <= len(scratch_off_dict):
            print("Calculating Card #"+str(card_num))
            numbers = scratch_off_dict[str(card_num)]['numbers']
            win_values = scratch_off_dict[str(card_num)]['win_values']
            card_total = 0
            for number in win_values:
                for value in numbers:
                    if value.strip() == number:
                        card_total += 1
            total_cards += scratch_sub_elements(scratch_off_dict, card_num, card_total)
            card_num += 1

    return total_cards


def analyze_scratch_pile(filename):

    points = 0

    with open(filename) as pile:
        for card in pile:
            card_value = 0
            broken_up = card.split(':')[1].strip().split('|')
            win_values, numbers = broken_up[0].split(), broken_up[1].split()

            for num in win_values:
                num = num.strip()
                for value in numbers:
                    if value.strip() == num:
                        if card_value == 0:
                            card_value = 1
                        else:
                            card_value *= 2
            points += card_value

    return points


def main():
    print(analyze_scratch_pile('scratch_cards.txt'))
    print(get_total_scratchers('scratch_cards.txt'))


if __name__ == '__main__':
    main()
