import math

def Part1(lines):
    wins = 1
    times = (lines[0].split())[1:]
    distances = (lines[1].split())[1:]
    for i in range(len(times)): # dist = s(t-s) = st - s^2 # -s^2 + st - dist = 0 # (-t +/- sqrt(t^2 -4*dist)) / -2
        t = int(times[i])
        d = int(distances[i]) + 1
        #print(f"{t}, {d}")
        press_times = [math.ceil((-t + math.sqrt(t**2 - 4*d)) / -2), math.floor((-t - math.sqrt(t**2 - 4*d)) / -2)]
        wins *= press_times[1] - press_times[0] + 1
        #print(press_times)

    return wins

def Part2(lines):
    wins = 1
    times = (lines[0].split())[1:]
    distances = (lines[1].split())[1:]
    t, d = '', ''
    for i in range(len(times)):
        t += times[i]
        d += distances[i]
    t = int(t)
    d = int(d)

    press_times = [math.ceil((-t + math.sqrt(t**2 - 4*d)) / -2), math.floor((-t - math.sqrt(t**2 - 4*d)) / -2)]
    wins = press_times[1] - press_times[0] + 1

    return wins

with open("input.txt", "r") as f:
    lines = f.readlines()

print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2(lines)}")
