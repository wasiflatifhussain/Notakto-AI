

def Sacrificer():  #used for sacrificing board that has 2 elements
    from main import boardA,boardB,boardC
    from main import moveStorer1stMove
    move=moveStorer1stMove[-1][0]
    if move=='A': name=boardA
    elif move=='B': name=boardB
    elif move=='C': name=boardC
    # print(move)
    if moveStorer1stMove[-1][1] in ['5','6','7','8'] and name[1][1]=='X':
        move+=str(4-(int(moveStorer1stMove[-1][1])-4))
    elif moveStorer1stMove[-1][1] in ['0','1','2','3'] and name[1][1]=='X':
        move+=str(4+(4-int(moveStorer1stMove[-1][1])))
    elif moveStorer1stMove[-1][1]=='4':
        move+=str(12-(int(moveStorer1stMove[-3][1])+4))
    elif name[1][1]!='X':
        if name[0][0]==name[0][1]!=name[0][2]: move+=str(name[0][2])
        elif name[0][1]==name[0][2]!=name[0][0]: move+=str(name[0][0])
        elif name[0][2]==name[0][0]!=name[0][1]: move+=str(name[0][1])
        elif name[1][0]==name[1][1]!=name[1][2]: move+=str(name[1][2])
        elif name[1][1]==name[1][2]!=name[1][0]: move+=str(name[1][0])
        elif name[1][0]==name[1][2]!=name[1][1]: move+=str(name[1][1])
        elif name[2][0]==name[2][1]!=name[2][2]: move+=str(name[2][2])
        elif name[2][1]==name[2][2]!=name[2][0]: move+=str(name[2][0])
        elif name[2][0]==name[2][2]!=name[2][1]: move+=str(name[2][1])
        elif name[0][0]==name[1][0]!=name[2][0]: move+=str(name[2][0])
        elif name[0][0]==name[2][0]!=name[1][0]: move+=str(name[1][0])
        elif name[1][0]==name[2][0]!=name[0][0]: move+=str(name[0][0])
        elif name[0][1]==name[1][1]!=name[2][1]: move+=str(name[2][1])
        elif name[0][1]==name[2][1]!=name[1][1]: move+=str(name[1][1])
        elif name[1][1]==name[1][2]!=name[0][1]: move+=str(name[0][1])
        elif name[0][2]==name[1][2]!=name[2][2]: move+=str(name[2][2])
        elif name[0][2]==name[2][2]!=name[1][2]: move+=str(name[1][2])
        elif name[1][2]==name[2][2]!=name[0][2]: move+=str(name[0][2])
        elif name[0][0]==name[1][1]!=name[2][2]: move+=str(name[2][2])
        elif name[0][0]==name[2][2]!=name[1][1]: move+=str(name[1][1])
        elif name[1][1]==name[2][2]!=name[0][0]: move+=str(name[0][0])
        elif name[0][-1]==name[1][-2]!=name[2][-3]: move+=str(name[2][-3])
        elif name[0][-1]==name[2][-3]!=name[1][-2]: move+=str(name[1][-2])
        elif name[0][-2]==name[0][-3]!=name[0][-1]: move+=str(name[0][-1])

    return move