from easyAI import TwoPlayersGame, AI_Player, Negamax
from easyAI.Player import Human_Player

# Define a class that contains all the methods to play the game. Start by defining the players
# and who starts the game:
class GameController(TwoPlayersGame):
    def __init__(self, players):
        # Define the players
        self.players = players
        # Define who starts the game
        self.nplayer = 1

        #We will be using a 3×3 board numbered from one to nine row-wise:
        # Define the board
        self.board = [0] * 9

    # Define a method to compute all the possible moves:
    # Define possible moves
    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]

    #Define a method to update the board after making a move:
    # Make a move
    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    #Define a method to see if somebody has lost the game. We will be checking if somebody has three in a row:
    # Does the opponent have three in a line?
    def loss_condition(self):
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9],[1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
        return any([all([(self.board[i-1] == self.nopponent) for i in combination]) for combination in possible_combinations])

    
    #Check if the game is over using the loss_condition method:
    # Check if the game is over
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    #Define a method to show the current progress:
    # Show current position
    def show(self):
        print('\n'+'\n'.join([' '.join([['. ', 'O', 'X'][self.board[3*j + i]] for i in range(3)]) for j in range(3)]))

    #Compute the score using the loss_condition method:
    # Compute the score
    def scoring(self):
        return -100 if self.loss_condition() else 0

if __name__ == "__main__":
    # Define the algorithm
    algorithm = Negamax(7)

    # Start the game
    GameController([Human_Player(), AI_Player(algorithm)]).play()