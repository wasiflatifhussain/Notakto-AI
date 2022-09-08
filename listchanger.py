

def listChanger(board,pos1,pos2,var="X"):  #this InvalidChecktion changes the number to X from the integer
    from main import boardA,boardB,boardC
    from main import moveStorer1stMove
    from firstline import firstLine
    from printBoard import printBoard
    board[pos1][pos2]=var
    if firstLine()!=None: print(firstLine())
    else: firstLine()
    printBoard()