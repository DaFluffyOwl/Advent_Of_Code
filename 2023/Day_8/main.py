from math import lcm
def Part1(lines):
    directions = lines[0].strip()
    curr_loc = "AAA"
    index = 0
    destinations = {}
    remove = "(),"
    
    for line in lines:
        for char in remove:
            line = line.replace(char, "")
        if line != lines[0] and line != lines[1]:
            destinations[(line.split())[0]] = (line.split())[2:]

    while(curr_loc != "ZZZ"):
        match directions[index % len(directions)]:
            case "L":
                curr_loc = destinations[curr_loc][0]
            case "R":
                curr_loc = destinations[curr_loc][1]
        index += 1
    return index 

def Part2(lines):
    directions = lines[0].strip()
    curr_loc = 'A'
    loops_size = []
    index = 0
    destinations = {}
    remove = "(),"
    
    for line in lines:
        for char in remove:
            line = line.replace(char, "")
        if line != lines[0] and line != lines[1]:
            location = (line.split())[0]
            if location[-1] == 'A':
                location = location[-1]
            destination = (line.split())[2:]
            if location not in destinations.keys():
                destinations[location] = destination
            else:
                destinations[location].extend(destination)

    for i in range(0, int(len(destinations['A'])/2)):
        while(curr_loc[-1] != 'Z'):
            match directions[index % len(directions)]:
                case "L":
                    curr_loc = (destinations[curr_loc])[(i*2) % (len(destinations[curr_loc]))]
                case "R":
                    curr_loc = (destinations[curr_loc])[(1 + i*2) % (len(destinations[curr_loc]))]
            index += 1
        loops_size.append(index)
        curr_loc = 'A'
        index = 0
    return lcm(*loops_size)

with open("input.txt", "r") as f:
    lines = f.readlines()

print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2(lines)}")