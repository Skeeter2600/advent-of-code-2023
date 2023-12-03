

def gridify(filename):
    with open(filename) as schematic:
        grid_data = [list(i.strip().split()[0]) for i in schematic.readlines()]
    return grid_data


def find_parts(filename):
    def check_valid():
        return (value != '.' and not value.isnumeric()) or valid_number

    found_parts_sum = 0
    number_section = False
    valid_number = False
    line_count = 0
    working_number = ''

    data_grid = gridify(filename)

    for line in data_grid:
        index = 0

        for char in line:
            if str(char).isnumeric():
                number_section = True
                working_number = working_number + str(char)
                if line_count > 0:
                    # directly above
                    value = str(data_grid[line_count-1][index])
                    valid_number = check_valid()
                    if index > 0:
                        # above and left
                        value = str(data_grid[line_count-1][index-1])
                        valid_number = check_valid()
                    if index < len(line)-1:
                        # above and right
                        value = str(data_grid[line_count-1][index+1])
                        valid_number = check_valid()
                if index > 0:
                    # left value
                    value = str(line[index-1])
                    valid_number = check_valid()
                if index < len(line)-1:
                    # right value
                    value = str(line[index+1])
                    valid_number = check_valid()
                if line_count < len(data_grid)-1:
                    # directly below
                    value = str(data_grid[line_count+1][index])
                    valid_number = check_valid()
                    if index > 0:
                        # down and left
                        value = str(data_grid[line_count+1][index-1])
                        valid_number = check_valid()
                    if index < len(line)-1:
                        # down and right
                        value = str(data_grid[line_count+1][index+1])
                        valid_number = check_valid()

            elif number_section:
                if valid_number:
                    found_parts_sum += int(working_number)
                working_number = ''
                number_section = False
                valid_number = False

            index += 1

        if valid_number:
            found_parts_sum += int(working_number)
        working_number = ''
        number_section = False
        valid_number = False
        line_count += 1

    return found_parts_sum


def main():
    print(find_parts('part_data.txt'))


if __name__ == '__main__':
    main()
