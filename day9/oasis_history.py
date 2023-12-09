

def read_oasis_future(filename):
    next_number_total = 0

    with open(filename) as patterns:
        for pattern in patterns:
            pattern = pattern.split()
            pattern_layers = [pattern]
            break_cond = True

            # do layers
            while break_cond:
                i = 0
                current_diffs = []
                while i < len(pattern)-1:
                    current_diffs.append(int(pattern[i+1]) - int(pattern[i]))
                    i += 1
                if not any(current_diffs):
                    pattern_layers.append(current_diffs)
                    break_cond = False
                else:
                    pattern_layers.append(current_diffs)
                    pattern = current_diffs

            # calculate next
            value = 0
            for element in pattern_layers[::-1]:
                value = value + int(element[len(element)-1])

            next_number_total += value

    return next_number_total


def read_oasis_past(filename):
    next_number_total = 0

    with open(filename) as patterns:
        for pattern in patterns:
            pattern = pattern.split()
            pattern_layers = [pattern]
            break_cond = True

            # do layers
            while break_cond:
                i = 0
                current_diffs = []
                while i < len(pattern)-1:
                    current_diffs.append(int(pattern[i+1]) - int(pattern[i]))
                    i += 1
                if not any(current_diffs):
                    pattern_layers.append(current_diffs)
                    break_cond = False
                else:
                    pattern_layers.append(current_diffs)
                    pattern = current_diffs

            # calculate next
            value = 0
            for element in pattern_layers[::-1]:
                value = int(element[0]) - value

            next_number_total += value

    return next_number_total


def main():
    print(read_oasis_future('oasis_data.txt'))
    print(read_oasis_past('oasis_data.txt'))


if __name__ == '__main__':
    main()
