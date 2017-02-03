from eightQueens import *

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

            for yy in range(8):
                    for xx in range(8):
                        place = PlaceQueen(board,yy,xx)
                        if place == True:
                            queens = queens + 1
                            
                        if queens == 8:
                            displayBoard(board)
                            
                       # if isBoardFull(board) == True:
                        #    break

                        for yyy in range(8):
                                for xxx in range(8):
                                    place = PlaceQueen(board,yyy,xxx)
                                    if place == True:
                                        queens = queens + 1
                                        
                                    if queens == 8:
                                        displayBoard(board)
                                        
                                   # if isBoardFull(board) == True:
                                    #    break
                                    
                                    for yyyy in range(8):
                                            for xxxx in range(8):
                                                place = PlaceQueen(board,yyyy,xxxx)
                                                if place == True:
                                                    queens = queens + 1
                                                    
                                                if queens == 8:
                                                    displayBoard(board)
                                                    
                                                #if isBoardFull(board) == True:
                                                 #   break

                                                
                                                for yyyyy in range(8):
                                                        for xxxxx in range(8):
                                                            place = PlaceQueen(board,yyyyy,xxxxx)
                                                            if place == True:
                                                                queens = queens + 1
                                                                
                                                            if queens == 8:
                                                                displayBoard(board)
                                                                
                                                           # if isBoardFull(board) == True:
                                                            #    break


                                                            
                                                            for yyyyyy in range(8):
                                                                    for xxxxxx in range(8):
                                                                        place = PlaceQueen(board,yyyyyy,xxxxxx)
                                                                        if place == True:
                                                                            queens = queens + 1
                                                                            
                                                                        if queens == 8:
                                                                            displayBoard(board)
                                                                            
                                                                        #if isBoardFull(board) == True:
                                                                        #    break

                                                                                    
                                                                        for yyyyyyy in range(8):
                                                                                for xxxxxxx in range(8):
                                                                                    place = PlaceQueen(board,yyyyyyy,xxxxxxx)
                                                                                    if place == True:
                                                                                        queens = queens + 1
                                                                                        
                                                                                    if queens == 8:
                                                                                        displayBoard(board)
                                                                                        
                                                                                    #if isBoardFull(board) == True:
                                                                                     #   break
                                                                                                            
                                                                                    for yyyyyyyy in range(8):
                                                                                            for xxxxxxxx in range(8):
                                                                                                place = PlaceQueen(board,yyyyyyyy,xxxxxxxx)
                                                                                                if place == True:
                                                                                                    queens = queens + 1
                                                                                                    
                                                                                                if queens == 8:
                                                                                                    displayBoard(board)
                                                                                                    
                                                                                                #if isBoardFull(board) == True:
                                                                                                    #break

                                                                                                #displayBoard(board)


