from eightQueens import *

queens = 0

iteration = 0


board = createBoard()

for y in range(8):
        for x in range(8):                      
                if placeQueen(board,y,x) == True:
                        queens = queens + 1
                        freeSquares = freeSpaces(board)       
                        
                for square in freeSquares:
                        
                        if placeQueen(board,freeSquares[0][0],freeSquares[0][1]) == True:
                                queens = queens + 1
                                freeSquares = freeSpaces(board)
                                                     
                        
                        if queens > 5:
                                displayBoard(board)
                                board = createBoard()
                                queens = 0

                
                        if isBoardFull == True:
                                board = createBoard()
                                queens = 0
                                
                                             
        

