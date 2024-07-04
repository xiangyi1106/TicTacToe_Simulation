class Tictactoe:
    
    def __init__(self):
        self.ttt = {
            'top-l': '', 'top-c': '', 'top-r': '',
            'mid-l': '', 'mid-c': '', 'mid-r': '',
            'bot-l': '', 'bot-c': '', 'bot-r': '',
        }
        self.player = 'X'

    # Print the tile
    def print_tile(self): 
        print(self.ttt['top-l'], ' |', self.ttt['top-c'], ' |', self.ttt['top-r'])
        print('- + - + -')
        print(self.ttt['mid-l'], ' |', self.ttt['mid-c'], ' |', self.ttt['mid-r'])
        print('- + - + -')
        print(self.ttt['bot-l'], ' |', self.ttt['bot-c'], ' |', self.ttt['bot-r'])

    def check_winner(self):
        winning_combinations = [
            ['top-l', 'top-c', 'top-r'],
            ['mid-l', 'mid-c', 'mid-r'],
            ['bot-l', 'bot-c', 'bot-r'],
            ['top-l', 'mid-l', 'bot-l'],
            ['top-c', 'mid-c', 'bot-c'],
            ['top-r', 'mid-r', 'bot-r'],
            ['top-l', 'mid-c', 'bot-r'],
            ['top-r', 'mid-c', 'bot-l'],
        ]
        for combo in winning_combinations:
            # Check if the three continuous positions are owned by the same player and they are not empty
            if self.ttt[combo[0]] == self.ttt[combo[1]] == self.ttt[combo[2]] and self.ttt[combo[0]] != '':
                # Return the winner player (either X or O)
                return self.ttt[combo[0]]
        return None

    def is_board_full(self):
        for key in self.ttt:
            if self.ttt[key] == '':
                return False
        return True

    def play_tictactoe(self):

        # Print game instructions
        print("Instruction:")
        print("Player 1 is 'X', and Player 2 is 'O'. Players take turns to make their moves by entering the position.")
        print("Possible positions that can be entered are: ")
        print("top-l (top left), top-c (top center), top-r (top right),")
        print("mid-l (middle left), mid-c (middle center), mid-r (middle right),")
        print("bot-l (bottom left), bot-c (bottom center), bot-r (bottom right).")
        print("The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins!")

        print("\nGame Start!\n")
        
        while True:  
            self.print_tile()
            print("")
            
            position = input("Turn for " + self.player + ". Move to which space? Eg:(top-l/c/r, mid-l/c/r, bot-l/c/r)")
            
            # Check if the input is one of the dictionary keys
            if position in self.ttt:
                
                # Check if the position is empty
                if self.ttt[position] == '':
                    self.ttt[position] = self.player
                    
                    #Check whether there is a winner
                    winner = self.check_winner()
                    
                    if winner:
                        self.print_tile()
                        print(f"Congratulations! {winner} wins!")
                        break  # Exit the loop if there is a winner

                    if self.is_board_full():
                        self.print_tile()
                        print("It's a draw!")
                        break  # Exit the loop if it's a draw
                        
                    #Switch player
                    if self.player == 'O': 
                        self.player = 'X'
                    else: 
                        self.player = 'O'
                else:
                    print("This space is already occupied. Please try again.")
                    
            else:
                print("Invalid position. Please try again.")
                
            