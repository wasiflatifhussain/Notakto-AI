

def SpecialBootTrap():
    from main import boardA,boardB,boardC
    from main import moveStorer1stMove
    from main import selfSacrifice
    if selfSacrifice==1:
        if moveStorer1stMove[-1][0]=='B':
            move='C'
        elif moveStorer1stMove[-1][0]=='C':
            move='B'
    if move=='A': name=boardA
    elif move=='B': name=boardB
    elif move=='C': name=boardC
    if name[0][0]=='X' and name[2][1]!='X': move+=str(name[2][1])
    elif name[0][0]=='X' and name[1][2]!='X': move+=str(name[1][2])
    elif name[0][1]=='X' and name[2][2]!='X': move+=str(name[2][2])
    elif name[0][1]=='X' and name[2][0]!='X': move+=str(name[2][0])
    elif name[0][2]=='X' and name[2][1]!='X': move+=str(name[2][1])
    elif name[0][2]=='X' and name[1][0]!='X': move+=str(name[1][0])
    elif name[1][0]=='X' and name[0][2]!='X': move+=str(name[0][2])
    elif name[1][0]=='X' and name[2][2]!='X': move+=str(name[2][2])
    elif name[1][2]=='X' and name[0][0]!='X': move+=str(name[0][0])
    elif name[1][2]=='X' and name[2][0]!='X': move+=str(name[2][0])
    elif name[2][0]=='X' and name[0][1]!='X': move+=str(name[0][1])
    elif name[2][0]=='X' and name[1][2]!='X': move+=str(name[1][2])
    elif name[2][1]=='X' and name[0][0]!='X': move+=str(name[0][0])
    elif name[2][1]=='X' and name[0][2]!='X': move+=str(name[0][2])
    elif name[2][2]=='X' and name[1][0]!='X': move+=str(name[1][0])
    elif name[2][2]=='X' and name[0][1]!='X': move+=str(name[0][1])
    return move