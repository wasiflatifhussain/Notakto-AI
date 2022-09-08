import sys
from firstline import firstLine
from bootTrap import BootTrap
from centerX import CentreX
from lateSacrifice import LateSacrifice
from listchanger import listChanger
from printBoard import printBoard
from sacrificer import Sacrificer
from specialBootTrap import SpecialBootTrap
from specialCase import SpecialCase

boardA=[[0,1,2],[3,4,5],[6,7,8]]
boardB=[[0,1,2],[3,4,5],[6,7,8]]
boardC=[[0,1,2],[3,4,5],[6,7,8]]
x_check=list('X'*3)


# from main import boardA,boardB,boardC


# print(firstLine())
a=printBoard()
player='1'
InvalidCheck=True
aCount=0
aiCount=0
aitracker=0
firstMoveTrack=0
sacrifice=0
specialSacrifice=0
hideCase=0
specialCaseRun=0
selfSacrifice=0
moveStorer1stMove=[]
moveStorer2nd=[]
alphabets=['A','B','C']
continueCond = 0

while (continueCond == 0):
    if aitracker==0 and aiCount==0: #this runs only for first time then stops
            move='A4'
            print('Super Smart AI: '+move)
            aitracker+=1
    elif aitracker!=0 and aiCount==0: #all your codes should be added here! MUST!
            if moveStorer1stMove[1][0]==moveStorer1stMove[0][0] and firstMoveTrack==0 and sacrifice!=2:  #if keeps playing boardA, to sacrifice boardA
                move=Sacrificer()
                sacrifice+=1
                print('Super Smart AI: '+move)
                
                firstMoveTrack+=1
            elif moveStorer1stMove[1][0]!=moveStorer1stMove[0][0] and firstMoveTrack==0:
                # for ele in alphabets:
                #     if ele!=moveStorer1stMove[0][0] and ele!=moveStorer1stMove[1][0]:
                #         move=ele+'4'
                move=CentreX()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1    

            elif len(moveStorer1stMove)==4 and sacrifice==0:  #this is for third move
                if moveStorer1stMove[-1][0]=='A':
                    move=Sacrificer()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    sacrifice+=1
                    # specialCaseRun+=1
                elif moveStorer1stMove[-1][0]=='B' and boardB[1][1]=='X':
                    move=Sacrificer()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    sacrifice+=1
                    specialSacrifice+=1
                elif moveStorer1stMove[-1][0]=='B' and boardB[1][1]!='X':
                    if moveStorer1stMove[-1][1]!='8' and moveStorer1stMove[-1][1]!='6' and moveStorer1stMove[-1][1]!='2' and moveStorer1stMove[-1][1]!='0':   
                        move=LateSacrifice()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        specialSacrifice+=1

                    elif moveStorer1stMove[-1][1]=='8' or moveStorer1stMove[-1][1]=='6' or moveStorer1stMove[-1][1]=='2' or moveStorer1stMove[-1][1]=='0':
                        move=Sacrificer()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        sacrifice+=1

                elif moveStorer1stMove[-1][0]=='C' and boardC[1][1]=='X':
                    move=Sacrificer()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    sacrifice+=1
                    # specialSacrifice+=1
                elif moveStorer1stMove[-1][0]=='C' and boardC[1][1]!='X':
                    if moveStorer1stMove[-1][1]!='8' and moveStorer1stMove[-1][1]!='6' and moveStorer1stMove[-1][1]!='2' and moveStorer1stMove[-1][1]!='0':
                        move=LateSacrifice()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        specialSacrifice+=1
                    elif moveStorer1stMove[-1][1]=='8' or moveStorer1stMove[-1][1]=='6' or moveStorer1stMove[-1][1]=='2' or moveStorer1stMove[-1][1]=='0':
                        move=Sacrificer()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        sacrifice+=1
            #give something else instead of true
            elif len(moveStorer1stMove)==4 and sacrifice==1:
                move=CentreX()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                # sacrifice+=1

            elif len(moveStorer1stMove)==4 and boardB[1][1]!='X' and sacrifice<2:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1

            elif len(moveStorer1stMove)==4 and boardC[1][1]!='X' and sacrifice<2:
                print(boardC)
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1

            elif len(moveStorer1stMove)==6 and boardB[1][1]!='X' and sacrifice<2 and specialSacrifice<1:
                if moveStorer1stMove[-1][0]=='B':
                    if moveStorer1stMove[-1][1]!='6' and moveStorer1stMove[-1][1]!='2' and moveStorer1stMove[-1][1]!='0':   
                        move=LateSacrifice()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        specialSacrifice+=1
                    elif moveStorer1stMove[-1][1]=='8' or moveStorer1stMove[-1][1]=='6' or moveStorer1stMove[-1][1]=='2' or moveStorer1stMove[-1][1]=='0':
                        move=Sacrificer()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        sacrifice+=1

                elif moveStorer1stMove[-1][0]=='C':
                    move=CentreX()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    hideCase+=1
                elif moveStorer1stMove[-1][0]=='A':
                    move=CentreX()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    hideCase+=1
                    aCount+=1
                    # break
                # elif moveStorer1stMove[-1][1]=='A':
                #     move=CentreX()
                #     print('Super Smart AI79: '+move)
                #     firstMoveTrack+=1

            elif len(moveStorer1stMove)==6 and boardC[1][1]!='X' and sacrifice<2 and specialSacrifice<1:
                if moveStorer1stMove[-1][0]=='C':
                    if moveStorer1stMove[-1][1]!='8' and moveStorer1stMove[-1][1]!='6' and moveStorer1stMove[-1][1]!='2' and moveStorer1stMove[-1][1]!='0':
                        move=LateSacrifice()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        specialSacrifice+=1
                    elif moveStorer1stMove[-1][1]=='8' or moveStorer1stMove[-1][1]=='6' or moveStorer1stMove[-1][1]=='2' or moveStorer1stMove[-1][1]=='0':
                        move=Sacrificer()
                        print('Super Smart AI: '+move)
                        firstMoveTrack+=1
                        sacrifice+=1
                    
                elif moveStorer1stMove[-1][0]=='B':
                    move=CentreX()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    hideCase+=1
                elif moveStorer1stMove[-1][0]=='A':
                    move=CentreX()
                    print('Super Smart AI: '+move)
                    firstMoveTrack+=1
                    hideCase+=1
                    aCount+=1

                # elif moveStorer1stMove[-1][1]=='A':
                #     move=CentreX()
                #     print('Super Smart AI79: '+move)
                #     firstMoveTrack+=1

            elif len(moveStorer1stMove)==6 and boardB[1][1]=='X' and sacrifice<2 and specialSacrifice<1:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1

            elif len(moveStorer1stMove)==6 and boardC[1][1]=='X' and sacrifice<2 and specialSacrifice<1:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1
                # specialCaseRun+=1

            elif len(moveStorer1stMove)==6 and boardB[1][1]=='X' and sacrifice<2 and specialSacrifice>=1:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1

            elif len(moveStorer1stMove)==6 and boardC[1][1]=='X' and sacrifice<2 and specialSacrifice>=1:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1     

            elif len(moveStorer1stMove)>=8 and sacrifice<2 and hideCase<1:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                sacrifice+=1


            elif len(moveStorer1stMove)>=8 and sacrifice>=2 and hideCase<1:
                move=BootTrap()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
            
            elif len(moveStorer1stMove)==8 and sacrifice==1 and hideCase==1 and selfSacrifice==0 and aCount==0:
                selfSacrifice+=1
                move=SpecialBootTrap()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
            
            elif len(moveStorer1stMove)==8 and hideCase>=1 and specialCaseRun<1:
                # if moveStorer1stMove[-1][0]=='B' :
                #     move='C'+moveStorer1stMove[-1][1]
                # elif moveStorer1stMove[-1][0]=='C':
                #     move='B'+moveStorer1stMove[-1][1]
                move=SpecialCase()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                specialCaseRun+=1
            
            # elif len(moveStorer1stMove)>=8 and sacrifice<=2 and hideCase>=1 and specialCaseRun<1:
            #     move=BootTrap()
            #     print('Super Smart AI2393: '+move)
            #     firstMoveTrack+=1
            
            elif len(moveStorer1stMove)>=8 and sacrifice<2 and hideCase>=1 and specialCaseRun<=1:
                move=Sacrificer()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                specialCaseRun+=1
                sacrifice+=1
            
            elif len(moveStorer1stMove)>=8 and sacrifice<=2 and hideCase>=1 and specialCaseRun>=1:
                # if moveStorer1stMove[-1][0]=='B': move='C'
                # elif moveStorer1stMove[-1][0]=='C': move='B'
                # groove=BootTrap()
                # move+=groove
                move=BootTrap()
                print('Super Smart AI: '+move)
                firstMoveTrack+=1
                specialCaseRun+=1
                # break
            # elif moveStorer1stMove[3]!='B4' and boardB[1][2]!='X':
            #     move='B4'
            #     print('Super Smart AI: '+move)
            #     firstMoveTrack+=1
            #     sacrifice+=1
            # elif moveStorer1stMove[3]!='C4' and boardC[1][2]!='X':
            #     move='C4'
            #     print('Super Smart AI: '+move)
            #     firstMoveTrack+=1
            #     sacrifice+=1



            else:
                move=input('Super Smart AI: ')
                # sacrifice+=1
            
            aitracker+=1
            

    elif aiCount==1:
        move=input('Omega Brain Human: ')
        # moveStorer1stMove.append(move)
        

    if len(move)<2:
        print("Invalid move, please input again")
        InvalidCheck=False
    elif move[0]!='A' and move[0]!='B' and move[0]!='C' or move[1].isnumeric()==False or move[1:].isnumeric()==False or int(move[1:])>8 or move[0] not in firstLine():
        print("Invalid move, please input again")
        InvalidCheck=False
    elif len(move)>2:
        print("Invalid move, please input again")
        InvalidCheck=False        
    if move[0]=='A' and InvalidCheck: #for valid movees, finding pos
        for i in range(len(boardA)): #these 3 clauses check the exact index where X should go
            for j in range(len(boardA)):
                if int(move[1])==boardA[i][j]:
                    pos1=i
                    pos2=j
                    break 
        if boardA[pos1][pos2]=='X':
            print("Invalid move, please input again")
            InvalidCheck=False
        else:                           
            listChanger(boardA,pos1,pos2)
    elif move[0]=='B' and InvalidCheck:
        for i in range(len(boardB)):
            for j in range(len(boardB)):
                if int(move[1])==boardB[i][j]:
                    pos1=i
                    pos2=j
                    break   
        if boardB[pos1][pos2]=='X':
            print("Invalid move, please input again")
            InvalidCheck=False                 
        else:
            listChanger(boardB,pos1,pos2)
    elif move[0]=='C' and InvalidCheck:
        for i in range(len(boardC)):
            for j in range(len(boardC)):
                if int(move[1])==boardC[i][j]:
                    pos1=i
                    pos2=j
                    break                    
        if boardC[pos1][pos2]=='X':
            print("Invalid move, please input again")
            InvalidCheck=False
        else:
            listChanger(boardC,pos1,pos2)
    if player=='1' and InvalidCheck: player='2'
    elif InvalidCheck: player='1'
    if firstLine()==None and player=='2':
        print('Omega Brain Human wins game')
        continueCond = 1    #new edit
        sys.exit()
        break
    elif firstLine()==None and player=='1':
        print('Super Smart AI wins game')
        continueCond = 1    #new edit
        sys.exit()
        break
    if InvalidCheck==True and aiCount==0:  #this is to interchange between P1 and P2 only if valid moves given
        aiCount=1
    elif InvalidCheck==True and aiCount==1:
        aiCount=0
    if InvalidCheck==True:
        moveStorer1stMove.append(move)
    InvalidCheck=True


    

    