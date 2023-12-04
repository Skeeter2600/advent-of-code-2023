

def gridify(filename):
    with open(filename) as schematic:
        grid_data = [list(i.strip().split()[0]) for i in schematic.readlines()]
    return grid_data


def gear_check(filename):

    def number_get(x, y):
        modified_coord = y-1
        start = str(data_grid[x][y])
        left = ''
        right = ''
        left_check = str(data_grid[x][modified_coord]).isnumeric()
        while left_check and modified_coord >= 0:
            left = str(data_grid[x][modified_coord]) + left
            modified_coord -= 1
            if modified_coord < 0:
                break
            left_check = str(data_grid[x][modified_coord]).isnumeric()

        modified_coord = y+1
        right_check = str(data_grid[x][modified_coord]).isnumeric()
        while right_check and modified_coord <= len(data_grid[x])-1:
            right = right + str(data_grid[x][modified_coord])
            modified_coord += 1
            if modified_coord > len(data_grid[x])-1:
                break
            right_check = str(data_grid[x][modified_coord]).isnumeric()

        return left + start + right

    found_gear_sum = 0
    line_count = 0


    data_grid = gridify(filename)

    for line in data_grid:
        index = 0

        for char in line:
            if char == '*':
                up_line = False
                down_line = False
                gear_one = 0
                gear_two = 0
                if line_count > 0:
                    # directly above
                    if str(data_grid[line_count-1][index]).isnumeric():
                        up_line = True
                        gear_one = number_get(line_count-1, index)
                    if index > 0:
                        # above and left
                        if str(data_grid[line_count-1][index-1]).isnumeric() and not up_line:
                            if gear_one == 0:
                                gear_one = number_get(line_count-1, index-1)
                            else:
                                gear_two = number_get(line_count-1, index-1)
                    if index < len(line)-1:
                        # above and right
                        if str(data_grid[line_count-1][index+1]).isnumeric() and not up_line:
                            if gear_one == 0:
                                gear_one = number_get(line_count-1, index+1)
                            else:
                                gear_two = number_get(line_count-1, index+1)
                if index > 0:
                    # left value
                    if str(line[index-1]).isnumeric():
                        if gear_one == 0:
                            gear_one = number_get(line_count, index-1)
                        else:
                            gear_two = number_get(line_count, index-1)
                if index < len(line)-1:
                    # right value
                    if str(line[index+1]).isnumeric():
                        if gear_one == 0:
                            gear_one = number_get(line_count, index+1)
                        else:
                            gear_two = number_get(line_count, index+1)
                if line_count < len(data_grid)-1:
                    # directly below
                    if str(data_grid[line_count+1][index]).isnumeric():
                        down_line = True
                        if gear_one == 0:
                            gear_one = number_get(line_count+1, index)
                        else:
                            gear_two = number_get(line_count+1, index)
                    if index > 0:
                        # down and left
                        if str(data_grid[line_count+1][index-1]).isnumeric() and not down_line:
                            if gear_one == 0:
                                gear_one = number_get(line_count+1, index-1)
                            else:
                                gear_two = number_get(line_count+1, index-1)
                    if index < len(line)-1:
                        # down and right
                        if str(data_grid[line_count+1][index+1]).isnumeric() and not down_line:
                            if gear_one == 0:
                                gear_one = number_get(line_count+1, index+1)
                            else:
                                gear_two = number_get(line_count+1, index+1)

                found_gear_sum += int(gear_one) * int(gear_two)

            index += 1
        line_count += 1

    return found_gear_sum


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
    print(gear_check('part_data.txt'))


if __name__ == '__main__':
    main()
