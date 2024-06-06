def Part1(lines):
    allowed = [12, 13, 14] #R, G, B
    count = [0, 0, 0]
    isPossible = False
    for line in lines:
        information  = line.split(":")
        game_information = information[1].split(";")
        for bag in game_information:
            info = bag.split(";")








filename = "input.txt"
with open(filename, "r") as f:
    lines = f.readlines()
Part1(lines)
