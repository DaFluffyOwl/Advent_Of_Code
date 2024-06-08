def Part1(lines):
    total_points = 0
    for game in lines:
        game_points = 0
        win_count = 0
        info = game.split(":")
        nums = "".join(info[1:]).strip().split("|")
        nums[0] = nums[0].strip().split(" ")
        nums[1] = nums[1].strip().split(" ")
        nums[1] = " ".join(nums[1]).strip().split()

        for w_num in nums[0]:
            for g_num in nums[1]:
                if w_num == g_num:
                    #print(f"{w_num}, {g_num}, {win_count}")
                    win_count += 1
                    if win_count == 1:
                        game_points += 1
                    else:
                        game_points = game_points * 2
        total_points += game_points
    return total_points

def Part2(lines):
    copies = []
    game_id = 0
    card_count = 0
    for game in lines:
        copies_added = 1
        card_count += 1
        win_count = 0
        info = game.split(":")
        game_id = int(("".join(info[0]).split())[1])
        nums = "".join(info[1:]).strip().split("|")
        nums[0] = nums[0].strip().split(" ")
        nums[1] = nums[1].strip().split(" ")
        nums[1] = " ".join(nums[1]).strip().split()
        for w_num in nums[0]:
            for g_num in nums[1]:
                if w_num == g_num:
                    if win_count < len(lines):
                        win_count += 1
                    #card_count += 1

        for copy in copies:
            if copy[0] <= game_id <= copy[1]:
                card_count += 1
                copies_added += 1

        for i in range(0, copies_added):
            copies.append([game_id, game_id + win_count])

        #print(f"{copies}, {card_count}")
    return card_count



with open("input.txt", "r") as f:
    lines = f.readlines()

print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2(lines)}")
