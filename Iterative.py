from eightQueens import *

queens = 0



board = createBoard()


"""starting condition"""

freeSquares = freeSpaces(board)

for step in range(len(freeSquares)):

        while len(freeSquares)>0:
                if placeQueen(board,freeSquares[step][0],freeSquares[step][1]) == True:
                        queens = queens + 1
                        freeSquares = freeSpaces(board)
                        displayBoard(board)
                
                        



                             
        

