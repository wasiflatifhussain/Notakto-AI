

def BootTrap():
    from main import boardA,boardB,boardC
    from main import moveStorer1stMove
    # if selfSacrifice==0:
    move=moveStorer1stMove[-1][0]
    # elif selfSacrifice==1:
    #     if moveStorer1stMove[-1][0]=='B':
    #         move='C'
    #     elif moveStorer1stMove[-1][0]=='C':
    #         move='B'
    if move=='A': name=boardA
    elif move=='B': name=boardB
    elif move=='C': name=boardC
    if moveStorer1stMove[-1][1]=='0' and name[1][2]!='X': move+=str(name[1][2])
    elif moveStorer1stMove[-1][1]=='0' and name[2][1]!='X': move+=str(name[2][1])
    elif moveStorer1stMove[-1][1]=='1' and name[2][0]!='X': move+=str(name[2][0])
    elif moveStorer1stMove[-1][1]=='1' and name[2][2]!='X': move+=str(name[2][2])
    elif moveStorer1stMove[-1][1]=='2' and name[2][1]!='X': move+=str(name[2][1])
    elif moveStorer1stMove[-1][1]=='2' and name[1][0]!='X': move+=str(name[1][0])
    elif moveStorer1stMove[-1][1]=='3' and name[0][2]!='X': move+=str(name[0][2])
    elif moveStorer1stMove[-1][1]=='3' and name[2][2]!='X': move+=str(name[2][2])
    elif moveStorer1stMove[-1][1]=='5' and name[0][0]!='X': move+=str(name[0][0])
    elif moveStorer1stMove[-1][1]=='5' and name[2][0]!='X': move+=str(name[2][0])
    elif moveStorer1stMove[-1][1]=='6' and name[1][2]!='X': move+=str(name[1][2])
    elif moveStorer1stMove[-1][1]=='6' and name[0][1]!='X': move+=str(name[0][1])
    elif moveStorer1stMove[-1][1]=='7' and name[0][0]!='X': move+=str(name[0][0])
    elif moveStorer1stMove[-1][1]=='7' and name[0][2]!='X': move+=str(name[0][2])
    elif moveStorer1stMove[-1][1]=='8' and name[0][1]!='X': move+=str(name[0][1])
    elif moveStorer1stMove[-1][1]=='8' and name[1][0]!='X': move+=str(name[1][0])
    return move