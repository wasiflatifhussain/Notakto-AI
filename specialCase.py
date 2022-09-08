

def SpecialCase():
    from main import boardA,boardB,boardC
    from main import moveStorer1stMove
    from main import aCount
    if moveStorer1stMove[-1][0]=='B' and aCount==0:
        move='C'
    elif moveStorer1stMove[-1][0]=='C' and aCount==0:
        move='B'
    elif moveStorer1stMove[-1][0]=='A' and aCount==1:
        move='A'
    if move=='A': name=boardA
    elif move=='B': name=boardB
    elif move=='C': name=boardC
    if moveStorer1stMove[-1][1]=='7' and name[0][0]=='X' or name[0][2]=='X': move+='7'
    elif moveStorer1stMove[-1][1]=='1' and name[2][0]=='X' or name[2][2]=='X': move+='1'
    return move