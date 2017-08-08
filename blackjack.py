class Player(object):
    def __init__(self,name):
        self.name = name
        self.money = 10000
        self.hand = []
    def hit(deck):
        hand.append(deck.deal)
    def set_bet(bet):
        money -= bet
        bet = bet
class Card(object):
    def __init__(self,suit,face):
        self.suit = suit
        self.face = face
        self.value = getvalue(face)
    def getvalue(face):
        if face >=2 and face <=10
            return face
        elif face > 10
            return 10
class Deck(object):
    def __init__(self):
        self.deck = []
        for s in range(4):
            for f in range(2,14)
                deck.append(Card(suit = s,face = f))
    def deal():
        return deck.pop()
def play_game():
    gamedeck = Deck()
    player = []
    print('Enter how many players would like to play.')
    plnum = input()
    for pl in range(plnum):
        print('What is your name?')
        plname = input()
        player[pl] = Player(name = plname)
