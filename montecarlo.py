class Game:
    def __init__(self, state, current_player):
        self.state = state
        self.current_player = current_player
    #jugadas validas
    def legal_moves(self, state, current_player):
        moves = []
        if current_player == 1:
            for i in range(6):
                if(state[i] !=0):
                    moves.append(i)
        else:
            for i in range(7,13):
                if(state[i] !=0):
                    moves.append(i)
        print(moves)
        return moves
    #hacer jugada
    def make_move(self, move):
        #revisar primero si cae en score
        beads = self.state[move]
        if self.current_player == 1:
            if (move + beads) % 6 == 0:
                #remove beads from current place
                self.state[move] = 0
                #add beads to score
                self.state[6] = self.state[6] + beads

    def win(state):
        #todo
        return winner

class Montecarlo:
    def __init__(self, parent, play, state, unexpanded_plays):
        self.play = play
        self.state = state
        self.plays = 0
        self.wins = 0
        self.parent = parent
        self.children = []
        
    def search_tree(self, state, timeout):
        #todo
    def best_play(self, state):
        #todo
        return best_choice
    
    
    
        
