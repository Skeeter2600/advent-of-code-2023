
def valid_game_maximums(filename):
    valid_games = 0

    with open(filename) as games:
        i = 1
        for line in games:
            valid = True
            grabs = line.strip().split(':')[1].split(';')
            for grab in grabs:
                cube_counts = grab.split(',')
                for cube_count in cube_counts:
                    values = cube_count.strip().split(' ')
                    color, number = values[1], int(values[0])
                    if color == 'blue' and number > 14:
                        valid = False
                    elif color == 'red' and number > 12:
                        valid = False
                    elif color == 'green' and number > 13:
                        valid = False
            if valid:
                valid_games += i
            i += 1

    return valid_games


def valid_games_minimums(filename):
    valid_games = 0

    with open(filename) as games:
        for line in games:
            blue = 0
            red = 0
            green = 0
            grabs = line.strip().split(':')[1].split(';')
            for grab in grabs:
                cube_counts = grab.split(',')
                for cube_count in cube_counts:
                    values = cube_count.strip().split(' ')
                    color, number = values[1], int(values[0])
                    if color == 'blue':
                        blue = max(blue, number)
                    elif color == 'red':
                        red = max(red, number)
                    elif color == 'green':
                        green = max(green, number)
            valid_games += red* blue*green

    return valid_games


def main():
    print(valid_game_maximums('game_data.txt'))
    print(valid_games_minimums('game_data.txt'))


if __name__ == '__main__':
    main()