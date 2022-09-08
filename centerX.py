

def CentreX():
    from main import boardA,boardB,boardC
    from main import moveStorer1stMove
    alphabets=['A','B','C']
    for ele in alphabets:
        if ele!=moveStorer1stMove[-1][0] and ele!=moveStorer1stMove[0][0]:
            move=ele+'4'
        if moveStorer1stMove[-1][0]=='A' and boardB[1][1]!='X':
            move='B4'
            # global aCount
            # aCount=1
        if moveStorer1stMove[-1][0]=='A' and boardC[1][1]!='X':
            move='C4'
            # global aCount
            # aCount=1
    return move