from eightQueens import *
import copy
from itertools import permutations


queens = 0
iteration = 0
board = createBoard()

freeSquares = freeSpaces(board)



for y in range(8):
    for x in range(8):
        print (y + x)
        board = createBoard()
        queens = 1
        placeQueen(board,y,x)
        freeSquares = freeSpaces(board)

        running = 0
        
        for p in permutations(freeSquares):
            print(p)
            for i in p:
                #print (i[0],i[1])
                if placeQueen(board,i[0],i[1]) == True:
                    queens = queens + 1
                    #print(queens)
                if queens > 7:
                    displayBoard(board)
                    board = createBoard()
                    placeQueen(board,y,x)
                    queens = 1
                    next
                if isBoardFull(board) == True:
                    board = createBoard()
                    placeQueen(board,y,x)
                    queens = 1
                    next 
                
            
        
            
        
        
        




        




                

