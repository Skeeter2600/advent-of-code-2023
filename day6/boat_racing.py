

def possible_speeds_big(filename):
    data = []

    with open(filename) as data_values:
        for line in data_values:
            line = line.strip().split(':')[1].split()

            if not data:
                data = ["".join(line)]
            else:
                distance = "".join(line)
                data[0] = [data[0],  distance]

    j = 1
    possibilities = 0
    while j < int(data[0][0]):
        if (int(data[0][0])-j)*j > int(data[0][1]):
            possibilities += 1
        else:
            if possibilities > 0:
                break
        j += 1

    return possibilities


def possible_speeds(filename):
    speed_product = 0
    data = []

    with open(filename) as data_values:
        for line in data_values:
            line = line.strip().split(':')[1].split()

            if not data:
                data = line
            else:
                i = 0
                for element in line:
                    data[i] = [data[i], element]
                    i += 1

    for pairing in data:
        j = 1
        possibilities = 0
        while j < int(pairing[0]):
            if (int(pairing[0])-j)*j > int(pairing[1]):
                possibilities += 1
            j += 1
        if speed_product == 0:
            speed_product = possibilities
        else:
            speed_product *= possibilities

    return speed_product


def main():
    print(possible_speeds('race_data.txt'))
    print(possible_speeds_big('race_data.txt'))


if __name__ == '__main__':
    main()
