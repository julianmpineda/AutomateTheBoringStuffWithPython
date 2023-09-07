import random
import sys
import time

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])

def checkWin(board, posOne, posTwo, posThree):
    if board[posOne] != ' ' and board[posOne] == board[posTwo] and board[posThree] == board[posTwo]:
        return True
    else:
        return False

def checkBoard(board, winSets):
    for sets in range(0,8):
        places = winSets[sets]
        win = checkWin(board, places[0], places[1], places[2])
        if win == True:
            if board[places[0]] == player:
                print('Player wins!')
                sys.exit()
            else:
                print('Computer wins!')
                sys.exit()

board = {'top-l' : ' ', 'top-m' : ' ', 'top-r' : ' ',
         'mid-l' : ' ', 'mid-m' : ' ', 'mid-r' : ' ',
         'bot-l' : ' ', 'bot-m' : ' ', 'bot-r' : ' '}

winSets = [['top-l', 'top-m', 'top-r'],
           ['mid-l', 'mid-m', 'mid-r'],
           ['bot-l', 'bot-m', 'bot-r'],
           ['top-l', 'mid-l', 'bot-l'],
           ['top-m', 'mid-m', 'bot-m'],
           ['top-r', 'mid-r', 'bot-r'],
           ['top-l', 'mid-m', 'bot-r'],
           ['top-r', 'mid-m', 'bot-l']]

win = False
player = ' '
computer = ' '
turns = 0

print('Do you want to be O or X?')

# checks to see if player input is correct
while player != 'X' or player != 'O':
    player = input()

    if player == 'X':
        computer = 'O'
        break
    elif player == 'O':
        computer = 'X'
        break
    else:
        print('Please enter X or O')

# checks to see board, computer places randomly on empty space
while turns < 9:
    print('Where do you want to place your marker?')
    place = input()
    
    while place not in board.keys() or board[place] != ' ':
        print('Please enter a valid space.')
        place = input()
    
    board[place] = player
    printBoard(board)
    checkBoard(board, winSets)
    turns += 1

    if turns == 9:
        break

    print('Computer is thinking...')
    time.sleep(random.randint(1,3))
    
    compPlace = random.choice(list(board.keys()))
    while board[compPlace] != ' ':
        compPlace = random.choice(list(board.keys()))

    board[compPlace] = computer
    
    print('Computer places ' + computer + ' on space: ' + compPlace)
    printBoard(board)

    checkBoard(board, winSets)
    turns += 1

print('It was a draw!')
sys.exit()

