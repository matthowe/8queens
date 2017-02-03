from eightQueens import *

def place(board, queens):
    for y in range(8):
            for x in range(8):              
               
               
                place = PlaceQueen(board,y,x)
                if place == True:
                    queens = queens + 1
                    
                if queens == 8:
                    displayBoard(board)
                    return
                    
                if isBoardFull(board) == True:
                    return

                



queens = 0

iteration = 0

board=createBoard()
iteration = place(board, queens)
displayBoard(board)
  


