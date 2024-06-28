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
    
    def convertJoker(self):
        c_joker = ''
        c_game = []

        if self.game == 'JJJJJ':
            return "AAAAA"
        for card in self.game:
            if c_joker == '' and card != 'J':
                c_joker = card
            if card != 'J' and card != '' and self.cards[card] > self.cards[c_joker]:
                c_joker = card
            elif card != 'J' and card != '' and self.cards[card] == self.cards[c_joker] and joker_hierarchy.index(card) < joker_hierarchy.index(c_joker):
                c_joker = card

        for card in self.game:
            if card == "J":
                c_game.append(c_joker)
            else:
                c_game.append(card)
        return "".join(c_game)



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
        

        
hierarchy = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
joker_hierarchy = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
            
def Part1(lines):
    games = list()
    for line in lines:
        #if game.is5ofKind():
            #rank.append([game.cards, (line.split())[1], '5'])
        g = line.split()
        games.append([g[0], g[1], Cardgame(g[0]).Classify()])
    
    games.sort(key=lambda x: x[2])
    #print(games)

    unsolved = True
    while(unsolved):
        #print(games)
        unsolved = False
        for i in range(0, len(games)): # Don't even try to figure this one out, but its basically insertion sort lol
            try:
                if Cardgame(games[i][0]).Classify() == Cardgame(games[i+1][0]).Classify():           
                    for j in range(0, len(games[i][0])):
                        if hierarchy.index(games[i][0][j]) < hierarchy.index(games[i+1][0][j]):
                            buffer = games[i]
                            games[i] = games[i+1]
                            games[i+1] = buffer
                            unsolved = True
                            break
                        elif hierarchy.index(games[i][0][j]) > hierarchy.index(games[i+1][0][j]):
                            break
            except:
                continue
    total = 0
    for i in range(0, len(games)):
        total += (i + 1) * int(games[i][1])
    #print(games)
    return total
    

def Part2(lines):
    games = list()
    for line in lines:
        g = line.split()
        games.append([g[0], g[1], Cardgame(Cardgame(g[0]).convertJoker()).Classify()])
    
    games.sort(key=lambda x: x[2])
    #print(games)

    unsolved = True
    while(unsolved):
        #print(games)
        unsolved = False
        for i in range(0, len(games)): # Don't even try to figure this one out, but its basically insertion sort lol
            try:
                if Cardgame(Cardgame(games[i][0]).convertJoker()).Classify() == Cardgame(Cardgame(games[i+1][0]).convertJoker()).Classify():           
                    for j in range(0, len(games[i][0])):
                        if joker_hierarchy.index(games[i][0][j]) < joker_hierarchy.index(games[i+1][0][j]):
                            buffer = games[i]
                            games[i] = games[i+1]
                            games[i+1] = buffer
                            unsolved = True
                            break
                        elif joker_hierarchy.index(games[i][0][j]) > joker_hierarchy.index(games[i+1][0][j]):
                            break
            except:
                continue
    total = 0
    for i in range(0, len(games)):
        total += (i + 1) * int(games[i][1])
    #print(games)
    return total

with open("input.txt", "r") as f:
    lines = f.readlines()
print(f"Part 1: {Part1(lines)}")
print(f"Part 2: {Part2(lines)}")