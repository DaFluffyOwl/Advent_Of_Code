#Part 1
def Part1():
    with open("input.txt") as f:
        lines = f.readlines()
    total = 0
    for l in lines:
        firstnum = -1
        secnum = -1
        for char in l:
            if firstnum == -1:
                if char.isnumeric():
                    firstnum = int(char)
            else:
                if char.isnumeric():
                    secnum = int(char)
        #print(f"{firstnum}, {secnum}")
        if secnum == -1:
            secnum = firstnum
        total = total + 10*firstnum + secnum

    print(total)

#Part 2
def Part2(fileName):
    total = 0
    with open(fileName) as f:
        lines = f.readlines()

    for l in lines:
        output = splitNums(l)
        #print("Newline")
        #print(f"{output[0]}, {output[-1]}")
        total = total + 10*output[0] + output[-1]
    return total

def splitNums(line):
    numbers = {"zero" : 0,"one": 1,"two": 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
    output = []
    word = ""
    for char_idx in range(0, len(line)):
        if line[char_idx].isnumeric():
            output.append(int(line[char_idx]))
        else:
            for key in numbers.keys():
                word = ""
                try:
                    for index in range(0, len(key)):
                        word += line[char_idx + index]

                    #print(f"{word}, {key}\n")
                    if word in numbers:
                        output.append(numbers[word])
                        word = ""
                except:
                    word = ""
    return output

print(Part2("input.txt"))
