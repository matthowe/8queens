from eightQueens import *
import copy


def bruteForce(board,freeSquares,queens):
    freeSquares = freeSpaces(board)
    if len(freeSquares) = 0:
        return dead
    else:
        for i in range(len(freeSquares)):
        placeQueen(board,freeSquares[i][0],freeSquares[i][1])
        freeSquares = freeSpaces(board)

        if queens > 7:
            displayBoard(board)
            board = createBoard()
            queens = 0



queens = 0
iteration = 0
board = createBoard()



        



        
    
def archive():
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
                                                         
                            
                            if queens > 7:
                                    displayBoard(board)
                                    board = createBoard()
                                    queens = 0



                    print("reset board")
                    queens = 0
                    displayBoard(board)


                    board = createBoard()
                                



                

