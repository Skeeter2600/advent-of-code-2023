import re

NUM_DICT = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def calibrate_nums(filename):

    calibration_total = 0

    with open(filename) as coords:
        for line in coords:
            first = re.findall('[0-9]', line)[0]
            second = re.findall(r'[0-9]', line)[-1]
            calibration_total += int(first+second)
    return calibration_total


def calibrate_words(filename):

    calibration_total = 0

    with open(filename) as coords:
        for line in coords:
            line = line.strip()
            found = []
            for word in NUM_DICT.keys():
                # get first instance of each num word
                result = line.find(word)
                if result != -1:
                    found += [[result, NUM_DICT[word]]]

            for word in NUM_DICT.keys():
                # get first instance of each num word
                result = line.rfind(word)
                if result != -1:
                    found += [[result, NUM_DICT[word]]]

            for word in NUM_DICT.keys():
                # get first instance of each num digit
                result = line.find(str(NUM_DICT[str(word)]))
                if result != -1:
                    found += [[result, NUM_DICT[word]]]

            for word in NUM_DICT.keys():
                # get last instance of each num digit
                result = line.rfind(str(NUM_DICT[str(word)]))
                if result != -1:
                    found += [[result, NUM_DICT[word]]]

            first = [100000, 'error']
            second = [-1, 'error']
            for find in found:
                if find[0] <= first[0]:
                    first = find
                if find[0] >= second[0]:
                    second = find
            calibration_total += int(str(first[1]) + str(second[1]))

    return calibration_total


def main():
   # print(calibrate_nums('day_1_data.txt'))
    print(calibrate_words('day_1_data.txt'))


if __name__ == '__main__':
    main()
