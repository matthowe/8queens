from eightQueens import *
import copy

queens = 0

iteration = 0


board = createBoard()


for y in range(8):
        for x in range(8):
                print(y,x)
                if placeQueen(board,y,x) == True:
                        queens = queens + 1
                        freeSquares = freeSpaces(board)
                        boardBackup = copy.deepcopy(board)



                        
                        
                while len(freeSquares) > 0:
                        
                        if placeQueen(board,freeSquares[0][0],freeSquares[0][1]) == True:
                                queens = queens + 1
                                freeSquares.pop(0)
                                freeSquares = freeSpaces(board)
                                                     
                        
                        #if queens > 5:
                        #        displayBoard(board)
                        #        board = createBoard()
                        #        queens = 0

                        displayBoard(board)               

                print("reset board")
                board = copy.deepcopy(boardBackup)


                board = createBoard()
                                
                                             


                        

