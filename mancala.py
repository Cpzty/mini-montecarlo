from random import random, randint, choice
select_player = [1,2]

class Mancala:
    def __init__(self, state, player):
        self.state = state
        self.player = player
        self.patch = 0
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
        final_position = move + beads
        if self.player == 1:
            #caso 1
            #ultimo bead cae en score
            #jugador vuelve a mover
            if (final_position) % 6 == 0:
                #remove beads from current place
                self.state[move] = 0
                for i in range(1, beads + 1):
                    scyther = (move + i) % 12
                    self.state[scyther] = self.state[scyther] + 1
                return 1

            #ultimo caso o caso sencillo
            #se reparte 1 bead a cada posicion
            else:
                self.state[move] = 0
                for i in range(1, beads+1):
                    scyther = (move + i) % 12
                    self.state[scyther] = self.state[scyther] + 1
                    # subcaso el ultimo bead cae una casilla vacia
                    # se añaden el ultimo bead del jugador y los beads del enemigo a score del jugador
                if ((final_position) % 12 < 6 and self.state[final_position] == 1):
                    mirror = 12 - final_position
                    self.state[6] = self.state[6] + self.state[mirror] + 1
                    self.state[mirror] = 0
                    self.state[final_position] = 0
                return 2
        else:
            if (final_position) % 13 == 0:
                #remove beads from current place
                self.state[move] = 0
                self.patch = 0
                for i in range(1, beads + 1):
                    scyther = (move + i + self.patch) % 13
                    if scyther != 6:
                        self.state[scyther] = self.state[scyther] + 1
                    else:
                        self.state[scyther + 1] = self.state[scyther + 1] + 1
                        self.patch = self.patch + 1
                return 2

            #ultimo caso o caso sencillo
            #se reparte 1 bead a cada posicion
            else:
                self.state[move] = 0
                self.patch = 0
                for i in range(1, beads + 1):
                    scyther = (move + i + self.patch) % 13
                    if scyther != 6:
                        self.state[scyther] = self.state[scyther] + 1
                    else:
                        self.state[scyther + 1] = self.state[scyther + 1] + 1
                        self.patch = self.patch + 1
                    # subcaso el ultimo bead cae una casilla vacia
                    # se añaden el ultimo bead del jugador y los beads del enemigo a score del jugador
                if ((final_position) % 13 > 6 and self.state[final_position] == 1):
                    mirror = 12 - final_position
                    self.state[13] = self.state[13] + self.state[mirror] + 1
                    self.state[mirror] = 0
                    self.state[final_position] = 0
                return 1

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
            game.player = game.make_move(decision)
        else:
            print("bot is making a choice")
            game.player = 2
    else:
        if(human == 2):
            print("player turn")
            decision = int(input("what is your move?: "))
            game.player = game.make_move(decision)

        else:
            print("bot is making a move...")
            game.player = 1
            
            
        
        
        
#print(game.state)
#print(game.player)
#game.valid_moves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],1)
        
