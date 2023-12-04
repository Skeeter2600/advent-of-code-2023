

def analyze_scratch_pile(filename):

    points = 0

    with open(filename) as pile:
        for card in pile:
            card_value = 0
            broken_up = card.split(':')[1].strip().split('|')
            win_values, numbers = broken_up[0].split(' '), broken_up[1].split(' ')

            for num in win_values:
                num = num.strip()
                for value in numbers:
                    if value.strip() == num and num.isnumeric():
                        if card_value == 0:
                            card_value = 1
                        else:
                            card_value *= 2
            points += card_value

    return points


def main():
    print(analyze_scratch_pile('scratch_cards.txt'))


if __name__ == '__main__':
    main()
