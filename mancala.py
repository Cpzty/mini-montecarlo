from random import random, randint, choice
select_player = [1,2]

class Mancala:
    def __init__(self, state, player):
        self.state = state
        self.player = player
    #valid moves
    def valid_moves(self,state,player):
        moves = []
        if player == 1:
            for i in range(6):
                if(state[i] !=0):
                    moves.append(i)
        else:
            for i in range(7,13):
                if(state[i] !=0):
                    moves.append(i)
        print(moves)
        return moves

    def make_move(self, move):
        #revisar primero si cae en score
        beads = self.state[move]
        if self.player == 1:
            if (move + beads) % 6 == 0:
                #remove beads from current place
                self.state[move] = 0
                #add beads to score
                self.state[6] = self.state[6] + beads
            else:
                for i in range(1, beads+1):
                    scyther = (move + i) % 12
                    self.state[scyther] = self.state[scyther] + 1


game = Mancala([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 1)
human = choice(select_player)
if(human == 1):
    bot = 2
else:
    bot = 1

print("player turn: "+str(human))
print("bot turn: "+str(bot))

while True:
    print(game.state)
    if game.player == 1:
        if(human == 1):
            print("player turn")
            decision = int(input("what is your move?: "))
            game.make_move(decision)
            game.player = 2
        else:
            print("bot is making a choice")
            game.player = 2
    else:
        if(human == 2):
            print("player turn")
            decision = int(input("what is your move?: "))
            game.make_move(decision)
            game.player = 1
        else:
            print("bot is making a move...")
            game.player = 1
            
            
        
        
        
#print(game.state)
#print(game.player)
#game.valid_moves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],1)
        
