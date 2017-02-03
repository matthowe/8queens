
def createBoard():
    board = [["." for _ in range(8)] for _ in range(8)]
    return board

def displayBoard(board):
    for y in range(8):
        for x in range(8):
            print(board[y][x],end='')
        print()
    print()

def autoPlaceQueen(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == ".":
                board[y][x] = "Q"
                queenBlocks(board)
                return True
    return False

def PlaceQueen(board,y,x):
    if board[y][x] == ".":
        board[y][x] = "Q"
        queenBlocks(board)
        return True
    return False
        
def queenBlocks(board):
    """for x and y"""
    for y in range(8):
        for x in range(8):
            if board[y][x] == "Q":
                for xn in range(8):
                    if board[y][xn] == ".":
                        board[y][xn] = "X"
                for yn in range(8):
                        if board[yn][x] == ".":
                            board[yn][x] = "X"


                """diagonal y+x+"""
                yn = y
                for xn in range(x,8):
                    if board[yn][xn] == ".":
                        board[yn][xn] = "X"
                    if yn < 7:
                        yn=yn+1
                        
                """diagonal y+x-"""        
                yn = y
                for xn in range(x,-1,-1):
                    if board[yn][xn] == ".":
                        board[yn][xn] = "X"
                    if yn < 7:
                        yn=yn+1
                        
                """diagonal y-x+"""    
                xn = x
                for yn in range(y,-1,-1):
                    if board[yn][xn] == ".":
                        board[yn][xn] = "X"
                    if xn < 7:
                        xn=xn+1

                """diagonal y-x-"""    
                xn = x
                for yn in range(y,-1,-1):
                    if board[yn][xn] == ".":
                        board[yn][xn] = "X"
                    if xn > -1:
                        xn=xn-1
                    

def isBoardFull(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == ".":
                return False
    #print("board full")
    return True

                    




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

            for y in range(8):
                    for x in range(8):
                        place = PlaceQueen(board,y,x)
                        if place == True:
                            queens = queens + 1
                            
                        if queens == 8:
                            displayBoard(board)
                            
                       # if isBoardFull(board) == True:
                        #    break

                        for y in range(8):
                                for x in range(8):
                                    place = PlaceQueen(board,y,x)
                                    if place == True:
                                        queens = queens + 1
                                        
                                    if queens == 8:
                                        displayBoard(board)
                                        
                                   # if isBoardFull(board) == True:
                                    #    break
                                    
                                    for y in range(8):
                                            for x in range(8):
                                                place = PlaceQueen(board,y,x)
                                                if place == True:
                                                    queens = queens + 1
                                                    
                                                if queens == 8:
                                                    displayBoard(board)
                                                    
                                                #if isBoardFull(board) == True:
                                                 #   break

                                                
                                                for y in range(8):
                                                        for x in range(8):
                                                            place = PlaceQueen(board,y,x)
                                                            if place == True:
                                                                queens = queens + 1
                                                                
                                                            if queens == 8:
                                                                displayBoard(board)
                                                                
                                                           # if isBoardFull(board) == True:
                                                            #    break


                                                            
                                                            for y in range(8):
                                                                    for x in range(8):
                                                                        place = PlaceQueen(board,y,x)
                                                                        if place == True:
                                                                            queens = queens + 1
                                                                            
                                                                        if queens == 8:
                                                                            displayBoard(board)
                                                                            
                                                                        #if isBoardFull(board) == True:
                                                                        #    break

                                                                                    
                                                                        for y in range(8):
                                                                                for x in range(8):
                                                                                    place = PlaceQueen(board,y,x)
                                                                                    if place == True:
                                                                                        queens = queens + 1
                                                                                        
                                                                                    if queens == 8:
                                                                                        displayBoard(board)
                                                                                        
                                                                                    #if isBoardFull(board) == True:
                                                                                     #   break
                                                                                                            
                                                                                    for y in range(8):
                                                                                            for x in range(8):
                                                                                                place = PlaceQueen(board,y,x)
                                                                                                if place == True:
                                                                                                    queens = queens + 1
                                                                                                    
                                                                                                if queens == 8:
                                                                                                    displayBoard(board)
                                                                                                    
                                                                                                if isBoardFull(board) == True:
                                                                                                    break




                                                            








def place(board):
    iteration = 0
    for y in range(8):
            for x in range(8):
                iteration = iteration + 1
                print("running iteration",iteration)
                
                queens = 0
                
                place = PlaceQueen(board,y,x)
                if place == True:
                    queens = queens + 1
                    
                if queens == 8:
                    return True
                
                if isBoardFull == True:
                    return True

#for i in range(8):
#    place(board)
                                

                                                                                            
                                        


                                                                                                       
        



#for queen in range(8):
#    print()

#board[3][3] = "Q"



#for y in range(8):
#    for x in range(8):
#        board = createBoard()
#        board[y][x] = "Q"
#        queens = 1
#        queenBlocks(board)
#        place = True
#        while place == True:
#            place = placeQueen(board)
#            queens = queens + 1

#        displayBoard(board)


