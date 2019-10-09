from random import random, randint, choice
from copy import deepcopy
select_player = [1, 2]

class Mancala:
    def __init__(self, state, player):
        self.state = state
        self.player = player
        self.patch = 0
        self.finish = False
        self.fake_state = []


    #valid moves
    def valid_moves(self, state):
        moves = []
        if self.player == 1:
            for i in range(6):
                if(state[i] !=0):
                    moves.append(i)
        else:
            for i in range(7, 13):
                if(state[i] !=0):
                    moves.append(i)
        #print(moves)
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
                    scyther = (move + i) % 13
                    self.state[scyther] = self.state[scyther] + 1
                return 1

            #ultimo caso o caso sencillo
            #se reparte 1 bead a cada posicion
            else:
                self.state[move] = 0
                for i in range(1, beads+1):
                    scyther = (move + i) % 13
                    self.state[scyther] = self.state[scyther] + 1
                    # subcaso el ultimo bead cae una casilla vacia
                    # se añaden el ultimo bead del jugador y los beads del enemigo a score del jugador
                if ((final_position) % 13 < 6 and self.state[final_position % 13] == 1):
                    mirror = 12 - (final_position % 13)
                    self.state[6] = self.state[6] + self.state[mirror] + 1
                    self.state[mirror] = 0
                    self.state[final_position % 13] = 0
                return 2
        else:
            if (final_position) % 13 == 0:
                #remove beads from current place
                self.state[move] = 0
                self.patch = 0
                for i in range(1, beads + 1):
                    scyther = (move + i + self.patch) % 14
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
                    scyther = (move + i + self.patch) % 14
                    if scyther != 6:
                        self.state[scyther] = self.state[scyther] + 1
                    else:
                        self.state[scyther + 1] = self.state[scyther + 1] + 1
                        self.patch = self.patch + 1
                    # subcaso el ultimo bead cae una casilla vacia
                    # se añaden el ultimo bead del jugador y los beads del enemigo a score del jugador
                if ((final_position) % 14 > 6 and self.state[final_position % 14] == 1):
                    mirror = 12 - (final_position % 14)
                    self.state[13] = self.state[13] + self.state[mirror] + 1
                    self.state[mirror] = 0
                    self.state[final_position % 14] = 0
                return 1

    def make_move_fake(self, move, state):
        #revisar primero si cae en score
        beads = self.fake_state[move]
        final_position = move + beads
        if self.player == 1:
            #caso 1
            #ultimo bead cae en score
            #jugador vuelve a mover
            if (final_position) % 6 == 0:
                #remove beads from current place
                self.fake_state[move] = 0
                for i in range(1, beads + 1):
                    scyther = (move + i) % 13
                    self.fake_state[scyther] = self.fake_state[scyther] + 1
                return 1

            #ultimo caso o caso sencillo
            #se reparte 1 bead a cada posicion
            else:
                self.fake_state[move] = 0
                for i in range(1, beads+1):
                    scyther = (move + i) % 13
                    self.fake_state[scyther] = self.fake_state[scyther] + 1
                    # subcaso el ultimo bead cae una casilla vacia
                    # se añaden el ultimo bead del jugador y los beads del enemigo a score del jugador
                if ((final_position) % 13 < 6 and self.fake_state[final_position % 13] == 1):
                    mirror = 12 - (final_position % 13)
                    self.fake_state[6] = self.fake_state[6] + self.fake_state[mirror] + 1
                    self.fake_state[mirror] = 0
                    self.fake_state[final_position % 13] = 0
                return 2
        else:
            if (final_position) % 13 == 0:
                #remove beads from current place
                state[move] = 0
                self.patch = 0
                for i in range(1, beads + 1):
                    scyther = (move + i + self.patch) % 14
                    if scyther != 6:
                        state[scyther] = state[scyther] + 1
                    else:
                        state[scyther + 1] = state[scyther + 1] + 1
                        self.patch = self.patch + 1
                return 2


    def terminal_state(self):
        if(self.state[0] + self.state[1] + self.state[2] + self.state[3] + self.state[4] + self.state[5] == 0
        or self.state[7] + self.state[8] + self.state[9] + self.state[10] + self.state[11] + self.state[12] == 0):
            #quien termina el juego no es revisado bajo este pensamiento y por lo tanto se agregan los beads de cada jugador a su score aunque
            self.state[6] = self.state[6] + self.state[0] + self.state[1] + self.state[2] + self.state[3] + self.state[4] + self.state[5]
            self.state[13] = self.state[13] + self.state[7] + self.state[8] + self.state[9] + self.state[10] + self.state[11] + self.state[12]
            #set to 0
            self.state[0] = self.state[1] = self.state[2] = self.state[3] = self.state[4] = self.state[5] = 0
            self.state[7] = self.state[8] = self.state[9] = self.state[10] = self.state[11] = self.state[12] = 0
            self.finish = True

    def terminal_state_fake(self, state):
        if(state[0] + state[1] + state[2] + state[3] + state[4] + state[5] == 0
        or state[7] + state[8] + state[9] + state[10] + state[11] + state[12] == 0):
            #quien termina el juego no es revisado bajo este pensamiento y por lo tanto se agregan los beads de cada jugador a su score aunque
            state[6] = state[6] + state[0] + state[1] + state[2] + state[3] + state[4] + state[5]
            state[13] = state[13] + state[7] + state[8] + state[9] + state[10] + state[11] + state[12]
            #set to 0
            state[0] = state[1] = state[2] = state[3] = state[4] = state[5] = 0
            state[7] = state[8] = state[9] = state[10] = state[11] = state[12] = 0
            return True
        return False


    # montecarlo
    def montecarlo_search_tree(self, n):
        temp_state = deepcopy(self.state)
        count7 = 0
        count8 = 0
        count9 = 0
        count10 = 0
        count11 = 0
        count12 = 0
        jugadas_validas = self.valid_moves(self.state)
        for i in range(len(jugadas_validas)):
            #refresh state after each option is completed
            for j in range(n):
                self.fake_state = deepcopy(temp_state)
                juego_termino = False
                once = False
                while juego_termino == False:
                    if once == False: 
                        once = True
                        self.make_move_fake(jugadas_validas[i], self.fake_state)
                    bot1_moves = self.valid_moves(self.fake_state)
                    self.make_move_fake(choice(bot1_moves), self.fake_state)
                    if self.player == 1:
                        self.player = 2
                    else:
                        self.player = 1
                    juego_termino = self.terminal_state_fake(self.fake_state)
                if(jugadas_validas[i] == 7):
                    if(self.fake_state[13] > self.fake_state[6]):
                        count7 = count7 + 1
                    elif(self.fake_state[6] > self.fake_state[13]):
                        count7 = count7 - 1
                elif(jugadas_validas[i] == 8):
                    if (self.fake_state[13] > self.fake_state[6]):
                        count8 = count8 + 1
                    elif (self.fake_state[6] > self.fake_state[13]):
                        count8 = count8 - 1
                elif (jugadas_validas[i] == 9):
                    if (self.fake_state[13] > self.fake_state[6]):
                        count9 = count9 + 1
                    elif (self.fake_state[6] > self.fake_state[13]):
                        count9 = count9 - 1
                elif (jugadas_validas[i] == 10):
                    if (self.fake_state[13] > self.fake_state[6]):
                        count10 = count10 + 1
                    elif (self.fake_state[6] > self.fake_state[13]):
                        count10 = count10 - 1
                elif (jugadas_validas[i] == 11):
                    if (self.fake_state[13] > self.fake_state[6]):
                        count11 = count11 + 1
                    elif (self.fake_state[6] > self.fake_state[13]):
                        count11 = count11 - 1
                elif (jugadas_validas[i] == 12):
                    if (self.fake_state[13] > self.fake_state[6]):
                        count12 = count12 + 1
                    elif (self.fake_state[6] > self.fake_state[13]):
                        count12 = count12 - 1

        return [count7, count8, count9, count10, count11, count12]


def print_game(state, player):
    if(player == 2):
        print("\n")
        print("|", state[6], "| ", state[0:6])
        print(state[7:13], " |", state[13], "|")
        print("\n") 
    else:
        print("\n")
        print( "|", state[13], "| ", state[12], " ", state[11], " ", state[10], " ", state[9], " ", state[8], " ", state[7])
        print(state[0:6], " |", state[6], "|")
        print("\n") 

game = Mancala([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], 1)

#revisar que llevar todos a 0 termina el juego para los jugadores
#expect p1 victory
#game = Mancala([0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0], 1)
#pass
#expect p2 victory
#game = Mancala([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0], 1)
#expect draw
#game = Mancala([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0], 1)
#revisar que no se saltee la penultima posicion del otro jugador
#game = Mancala([0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 1, 0], 1)
#turno extra p1
#game = Mancala([0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0], 1)
#turno extra p2
#game = Mancala([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0], 1)

#all tests passed

#human = choice(select_player)
human = 1
if(human == 1):
    bot = 2
else:
    bot = 1

print("player turn: "+str(human))
print("bot turn: "+str(bot))

while game.finish == False:
    print_game(game.state, human)
    #print(game.state)
    if game.player == 1:
        #if(human == 1):
        print("player turn")
        decision = int(input("what is your move? (0-5): "))
        referee = game.valid_moves(game.state)
        if decision in referee:
            game.player = game.make_move(decision)
        else:
            print("invalid move")
            continue
    else:
        print("bot is making a choice")
        monte = game.montecarlo_search_tree(10000)
        game.player = 2
        print("monte antes",monte)
        if(max(monte) == 0):
            for i in range(len(monte)):
                if monte[i] == 0:
                    monte[i] = float("-inf")
        print("monte despues", monte)
        #print("monte2 ",monte)
        bot_choice = monte.index(max(monte)) + 7
        print("bot choice", bot_choice)
        referee = game.valid_moves(game.state)
        if bot_choice in referee:
            game.player = game.make_move(bot_choice)
        else:
            print("invalid move")
            continue
    # else:
    #     if(human == 2):
    #         print("player turn")
    #         decision = int(input("what is your move? (7-12): "))
    #         referee = game.valid_moves()
    #         if decision in referee:
    #             game.player = game.make_move(decision)
    #         else:
    #             print("invalid move")
    #             continue
    #
    #     else:
    #         print("bot is making a move...")
    #         game.player = 1
    game.terminal_state()
print(game.state)
if(game.state[6] > game.state[13]):
    print("p1 won")
elif(game.state[13] > game.state[6]):
    print("p2 won")
else:
    print("its a draw")

#print(game.state)
#print(game.player)
#game.valid_moves([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],1)