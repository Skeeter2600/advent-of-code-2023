
def map_reader(filename):
    instructions = ""
    map_data = {}

    with open(filename) as map_info:
        for line in map_info:
            line = line.strip()
            if '=' not in line and line != '':
                instructions = line
            elif line:
                line = line.split('=')
                left_and_right = line[1].strip().split(',')
                map_data[line[0].strip()] = {'L': left_and_right[0].strip()[1:], 'R': left_and_right[1].strip()[:-1]}

    return [instructions, map_data]


def navigate(filename):
    steps = 0
    attempts = 0

    processed_map = map_reader(filename)
    instructions, map_data = processed_map[0], processed_map[1]

    position = 'AAA'

    while attempts < 1000:  # just a safety thing
        for char in instructions:
            steps += 1
            position = map_data[position][char]
            if position == 'ZZZ':
                return steps
        attempts += 1

    return 'ERROR: MAXED OUT. Is there a solution?'


def main():
    print(navigate('map_data.txt'))


if __name__ == '__main__':
    main()
