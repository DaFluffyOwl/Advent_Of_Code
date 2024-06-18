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
        
            
def Part1(lines):
    for line in lines:
        game = Cardgame((line.split())[0])
    
    hierarchy = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']



with open("input.txt", "r") as f:
    lines = f.readlines()
print(f"Part 1: {Part1(lines)}")
