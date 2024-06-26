class Cardgame:
    def __init__(self, game):
        self.game = game
        self.cards = {}
        for card in self.game:
            if card in self.cards:
                self.cards[card] += 1
            else:
                self.cards[card] = 1

    def is5ofKind(self):
        for card in self.cards.keys():
            if self.cards[card] == 5:
                return True
        return False

    def is4ofKind(self):
        for card in self.cards.keys():
            if self.cards[card] == 4:
                return True
        return False
    
    def isFHouse(self):
        for card in self.cards.keys():
            if self.cards[card] == 3:
                for card in self.cards.keys():
                    if self.cards[card] == 2:
                        return True
        return False
    
    def is3ofKind(self):
        for card in self.cards.keys():
            if self.cards[card] == 3:
                return True
        return False
    
    def is2Pair(self):
        count = 0
        for card in self.cards.keys():
            if self.cards[card] == 2:
                count += 1
        if count == 2:
            return True
        return False

    def is1Pair(self):
        for card in self.cards.keys():
            if self.cards[card] == 2:
                return True
        return False

    def Classify(self):
        if self.is5ofKind():
            return 7
        elif self.is4ofKind():
            return 6
        elif self.isFHouse():
            return 5
        elif self.is3ofKind():
            return 4
        elif self.is2Pair():
            return 3
        elif self.is1Pair():
            return 2
        else:
            return 1 
        

        
            
def Part1(lines):
    games = list()
    for line in lines:
        #if game.is5ofKind():
            #rank.append([game.cards, (line.split())[1], '5'])
        g = line.split()
        games.append([g[0], g[1], Cardgame(g[0]).Classify()])
    
    games.sort(key=lambda x: x[2])
    print(games)

    hierarchy = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    unsolved = True
    while(unsolved):
        for i in range(0, len(games)): # Don't even try to figure this one out, but its basically insertion sort lol
            unsolved = False
            try:
                if Cardgame(games[i][0]).Classify() == Cardgame(games[i+1][0]).Classify():           
                    for j in range(0, len(games[i][0])):
                        if hierarchy.index(games[i][0][j]) < hierarchy.index(games[i+1][0][j]):
                            buffer = games[i]
                            games[i] = games[i+1]
                            games[i+1] = buffer
                            #unsolved = True
                            break
            except:
                continue
    total = 0
    for i in range(0, len(games)):
        total += (i + 1) * int(games[i][1])
    print(games)
    return total
    





with open("input.txt", "r") as f:
    lines = f.readlines()
print(f"Part 1: {Part1(lines)}")
