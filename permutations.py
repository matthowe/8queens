from eightQueens import *
import copy
from itertools import permutations


queens = 0
iteration = 0
board = createBoard()

freeSquares = freeSpaces(board)



for y in range(8):
    for x in range(8):
        board = createBoard()
        queens = 0
        placeQueen(board,y,x)
        freeSquares = freeSpaces(board)

        running = 0
        print("running permutations - do not touch")
        for p in permutations(freeSquares):
            #running = running  + 1
            #print("permutation running ", running)
            
            for i in p:
                #print (i[0],i[1])
                if placeQueen(board,i[0],i[1]) == True:
                    queens = queens + 1
                    #print(queens)
                if queens > 4:
                    displayBoard(board)
                    board = createBoard()
                    placeQueen(board,y,x)
                    queens = 0
                if isBoardFull(board) == True:
                    board = createBoard()
                    placeQueen(board,y,x)
                    queens = 0
                    break
                
            
        
            
        
        
        




        




                

