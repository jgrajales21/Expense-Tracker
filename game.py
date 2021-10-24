import random

def get_computer_move () :
    """
    signature: () -> str
    returns one of 'rock', 'paper' or 'scissors' each time it is called.
    """
    return random.choice (['rock' , 'paper' , 'scissors'])


def is_valid_move (move) :
    """
    signature: str -> bool
    returns True just in case the move is one of 'rock', 'paper', or 'scissors'
    """
    if move == 'rock' or move == 'paper' or move =='scissors':
        return True
    else:
        return False


def get_player_move () :
    """
    signature: () -> str
    returns the player's move, which must be one of 'rock', 'paper' or 'scissors'.
    """
    move = input("Please enter your move: ") 
    while is_valid_move(move) == False:
        print("I'm sorry but" ,move, "is not a valid move. Please choose either rock, paper, or scissors")
        move = input("Please enter your move: ")
    return move


def play_game () :
    """
    signature: () -> NoneType
    interactively conducts a game of rock-paper-scissors
    between the player and the computer.
    """
   
    player_score = 0
    computer_score = 0
   
    while player_score < 3 and computer_score < 3 :
        print('Player Score: ' + str(player_score) + "\tComputer Score: " + str(computer_score))
        gpm = get_player_move()
        gcm = get_computer_move()
        if gpm == 'rock' and gcm == 'scissors':
            print('The computer chose scissors.')
            print('rock beats scissors\nYou win this round!\n')
            player_score += 1
        elif gpm == 'paper' and gcm == 'rock':
            print('The computer chose rock.')
            print('paper beats rock\nYou win this round!\n')
            player_score += 1
        elif gpm == 'scissors' and gcm == 'paper':
            print('The computer chose paper.')
            print('scissors beats paper\nYou win this round!\n')
            player_score += 1
        elif gcm == 'rock' and  gpm == 'scissors':
            print('The computer chose rock.')
            print('rock beats scissors\nThe computer wins this round!\n')
            computer_score += 1
        elif gcm == 'paper' and gpm == 'rock':
            print('The computer chose paper.')
            print('paper beats rock\nThe computer wins this round!\n')
            computer_score += 1
        elif gcm == 'scissors' and gpm == 'paper':
            print('The computer chose scissors.')
            print('scissors beats paper\nThe computer wins this round!\n')
            computer_score += 1
        elif gcm == gpm: #can't write code on the same line as else 
            print('You both chose the same thing.\nThis round is a tie!\n')
            
    
    if player_score > computer_score:
        print('The human is the winner!')
    else:
        print('The computer is the winner!')
