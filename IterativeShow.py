from eightQueens import *

queens = 0

iteration = 0


for y in range(8):
        for x in range(8):
            board = createBoard()
            
            iteration = iteration + 1
            print("running iteration",iteration)
            
            queens = 0
            
            place = PlaceQueen(board,y,x)
            if place == True:
                queens = queens + 1
                
            if queens == 8:
                displayBoard(board)
                
            if isBoardFull(board) == True:
                break

            displayBoard(board)

