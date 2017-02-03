from eightQueens import *

queens = 0

iteration = 0


board = createBoard()

for i in range(2):
        for y in range(8):
                for x in range(8):
                        
                        if placeQueen(board,y,x) == True:
                                queens = queens + 1
                                
                        displayBoard(board)
                        
                        
                        if queens > 3:
                                displayBoard(board)
                                board = createBoard()
                                queens = 0


                        displayBoard(board)
                        if isBoardFull == True:
                                board = createBoard()
                                queens = 0
                                
                                             
                

