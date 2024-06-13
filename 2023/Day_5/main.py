import math
def Part1(lines):
    locations = []
    maps = []
    map_number = 0
    buffer = []
    seeds = (lines[0].split(":"))[1].split()
    curr = 0
    for line in lines:
        if not(line == "\n"):
            if (line.split())[1] == "map:" or (line.split())[0] == "seeds:":
                if not buffer == []:
                    maps.append(buffer)
                buffer = []
            else:
                buffer.append(line.split())
    maps.append(buffer) #Makes sure not too miss the last map

    for seed in seeds:
        curr = int(seed)
        for t_map in maps:
            for ranges in t_map:
                destination = int(ranges[0])
                source = int(ranges[1])
                r = int(ranges[2])
                if source <= curr <= source + r:
                    curr = destination + (curr - source)
                    break
        locations.append(curr)
    return min(locations)

def Part2_brute(lines):
    locations = []
    maps = []
    map_number = 0
    buffer = []
    seeds_range = (lines[0].split(":"))[1].split()
    curr = 0

    for line in lines:
        if not(line == "\n"):
            if (line.split())[1] == "map:" or (line.split())[0] == "seeds:":
                if not buffer == []:
                    maps.append(buffer)
                buffer = []
            else:
                buffer.append(line.split())
    maps.append(buffer) #Makes sure not too miss the last map

    for i in range(0, len(seeds_range), 2):
        s_begin = int(seeds_range[i])
        s_range = int(seeds_range[i+1])
        print(f"{s_begin}, {s_range}")
        for i in range(s_begin, s_begin + s_range):
            curr = i
            for t_map in maps:
                for ranges in t_map:
                    destination = int(ranges[0])
                    source = int(ranges[1])
                    r = int(ranges[2])
                    if source <= curr <= source + r:
                        curr = destination + (curr - source)
                        break
            #print((s_begin + s_range) - i)
            locations.append(curr)
        locations = [min(locations)]
        print(locations)
    return min(locations)

def Part2_reverse_brute(lines): #Reverse the maps and brute force locations
    locations = []
    maps = []
    map_number = 0
    buffer = []
    seeds = (lines[0].split(":"))[1].split()
    curr = 0

    for line in lines:
        if not(line == "\n"):
            if (line.split())[1] == "map:" or (line.split())[0] == "seeds:":
                if not buffer == []:
                    maps.append(buffer)
                buffer = []
            else:
                buffer.append(line.split())
    maps.append(buffer) #Makes sure not too miss the last map

    '''
    for i in range(0, len(seeds_range), 2):
        s_begin = int(seeds_range[i])
        s_range = int(seeds_range[i+1])
        s_end = s_begin + s_range
        s_rng = range(s_begin, s_end)
    '''
    upper_bound = 300000000
    maps.reverse()

    for i in range(0, upper_bound):
        print(f"{i}", end='\r')
        curr = i
        for t_map in maps:
            for ranges in t_map:
                destination = int(ranges[0])
                source = int(ranges[1])
                r = int(ranges[2])
                if destination <= curr <= destination + r:
                    curr = source + (curr - destination)
                    break
        for j in range(0, len(seeds), 2):
            s_begin = int(seeds[j])
            s_range = int(seeds[j+1])
            if s_begin <= curr < s_begin + s_range:
                return i




with open("input.txt", "r") as f:
    lines = f.readlines()

print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2_reverse_brute(lines)}")
