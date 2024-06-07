import math
def Part1(lines):
    line_length = len(lines[0].strip())
    full = ""
    total = 0
    for line in lines:
        full += "".join(line).strip()
    adjacent = [-1-line_length, -1*line_length, 1-line_length, -1, 1, -1+line_length, line_length, 1+line_length]
    hasSymbol = False
    numChecked = False
    numUsed = False
    number = 0
    digits = []
    for i in range(0, len(full)):
        if full[i].isnumeric():
            for offset in adjacent:
                try:
                    if not(full[i + offset] == '.' or full[i + offset].isnumeric() or (i + offset) < 0):
                        hasSymbol = True
                        #print(f"{full[i]}, {i}; {full[i + offset]}, {i + offset}, {offset}")
                except:
                    continue

            while(full[i].isnumeric()):
                if not numChecked:
                    digits.append(int(full[i]))
                i += 1
            numChecked = True
            print(hasSymbol)
            print(digits)
            if hasSymbol and not numUsed:
                for j in range(0, len(digits)):
                    number += 10**(len(digits) - 1 - j) * int(digits[j])
                numUsed = True
            print(number)
            hasSymbol = False
        else:
            digits = []
            numChecked = False
            numUsed = False


    return total

def Part2(lines):
    line_length = len(lines[0].strip())
    gear_ratio_sum = 0
    full = ""
    hasGear = False
    numChecked = False
    rearIndex = None
    gearChecked = False
    numbers = []
    curr_num = 0
    total = 0

    for line in lines:
        full += "".join(line).strip()

    for i in range(0, len(full)):
        if full[i].isnumeric():
            gearIndex = gearAdjacent(full, line_length, i)
            if not numChecked:
                curr_num = getNum(full, line_length, i)
                numChecked = True

            if not(gearIndex == None or gearChecked):
                numbers.append([curr_num, gearIndex])
                gearChecked = True

        else:
            numChecked = False
            gearChecked = False
    print(numbers)
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i][1] == numbers[j][1]:
                total += numbers[i][0] * numbers[j][0]
                print(f"{numbers[i][0]}, {numbers[j][0]}")
    return total


def gearAdjacent(full, line_length, curr_i):
    adjacent = [-1-line_length, -1*line_length, 1-line_length, -1, 1, -1+line_length, line_length, 1+line_length]
    for offset in adjacent:
        try:
            if full[curr_i + offset] == "*":
                return curr_i + offset
        except:
            continue
    return None

def getNum(full, line_length, curr_i):
    digits = []
    number= 0
    while(full[curr_i].isnumeric()):
        digits.append(int(full[curr_i]))
        curr_i += 1

    for j in range(0, len(digits)):
        number += 10**(len(digits) - 1 - j) * int(digits[j])

    return number


filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()

#print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2(lines)}")
