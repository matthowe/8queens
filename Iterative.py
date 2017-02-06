from eightQueens import *
import copy



def bruteForce(board,searchIndex,queens):
    """NOT done as a tree transversal"""
    
    freeSquares = freeSpaces(board)

    print(searchIndex)

    print(len(freeSquares))
    if len(freeSquares) > 0:

        if len(freeSquares) == 1:
            searchIndex = 0            
        
        placeQueen(board,freeSquares[searchIndex][0],freeSquares[searchIndex][1])
        freeSquares = freeSpaces(board)

        displayBoard(board) #debugging

        if queens > 7:
            displayBoard(board)
            board = createBoard()
            queens = 0
            return

        #if len(freeSquares) = 0:
        bruteForce(board, searchIndex, queens)

    return   



queens = 0
iteration = 0
board = createBoard()

freeSquares = freeSpaces(board)

for searchIndex in range(64):
    bruteForce(board, searchIndex, queens)

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
                                



                

