def Part1(lines):
    allowed = [12, 13, 14] #R, G, B
    count = [0, 0, 0]
    index = {"red" : 0, "green" : 1, "blue": 2}
    isPossible = True
    game_id_sum = 0
    for line in lines:
        isPossible = True
        information  = line.split(":")
        game_id = ("".join(information).split(" "))[1]
        game_information = information[1].split(";")
        for bag in game_information:
            info = bag.split(",")
            for values in info:
                values = "".join(values).strip().split(" ")
                count = int(values[0])
                color = values[1]
                if count > allowed[index[color]]:
                    isPossible = False
        if isPossible:
            game_id_sum += int(game_id)
    return game_id_sum

def Part2(lines):
    power = 0
    count = [0, 0, 0]
    index = {"red" : 0, "green" : 1, "blue": 2}
    for line in lines:
        information  = line.split(":")
        game_information = information[1].split(";")
        least_needed = [0, 0, 0]
        for bag in game_information:
            info = bag.split(",")
            for values in info:
                values = "".join(values).strip().split(" ")
                count = int(values[0])
                color = values[1]
                if least_needed[index[color]] < count:
                    least_needed[index[color]] = count
        power += least_needed[0] * least_needed[1] * least_needed[2]
    return power


filename = "input.txt"
path = "/home/ryans/Documents/Coding/Advent_Of_Code/2023/Day_2/"
with open(path + filename, "r") as f:
    lines = f.readlines()
print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2(lines)}")
