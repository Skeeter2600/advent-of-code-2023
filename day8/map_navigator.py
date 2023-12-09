from math import gcd


def map_reader(filename):
    instructions = ""
    map_data = {}
    ends_in_a = []

    with open(filename) as map_info:
        for line in map_info:
            line = line.strip()
            if '=' not in line and line != '':
                instructions = line
            elif line:
                line = line.split('=')
                left_and_right = line[1].strip().split(',')
                if line[0][2] == 'A':
                    ends_in_a.append(line[0].strip())
                map_data[line[0].strip()] = {'L': left_and_right[0].strip()[1:], 'R': left_and_right[1].strip()[:-1]}

    return [instructions, map_data, ends_in_a]


def ghost_navigate(filename):
    processed_map = map_reader(filename)
    instructions, map_data, ghost_starts = processed_map[0], processed_map[1], processed_map[2]

    ghost_steps = []

    """
    NOTE FOR LATER:
    Calculate how many steps to find the Z,
    then fund least common multiplier between them all
    THere are 6 values, find the LCM between 1, 2, 3, 4, 5, and 6
    """

    for element in ghost_starts:
        position = element
        steps = 0
        attempts = 0
        breaking = True
        while attempts < 1000 and breaking:  # just a safety thing
            for char in instructions:
                steps += 1
                position = map_data[position][char]
                if position[2] == 'Z':
                    print(element + " " + str(steps))
                    ghost_steps.append(steps)
                    breaking = False
        attempts += 1

    lcm = 1

    for i in ghost_steps:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


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
    print(ghost_navigate('map_data.txt'))


if __name__ == '__main__':
    main()
