

def printBoard(validA=True,validB=True,validC=True):  #this prints the whole board of the game
    from main import boardA,boardB,boardC
    # from main import moveStorer1stMove
    for j in range(len(boardA)):
            if boardA[0][0]==boardA[0][1]==boardA[0][2] or boardA[1][0]==boardA[1][1]==boardA[1][2] or boardA[2][0]==boardA[2][1]==boardA[2][2] or boardA[1][1]==boardA[2][2]==boardA[0][0] or boardA[0][2]==boardA[1][1]==boardA[2][0]:
                validA=False
                pass
            if boardA[0][0]==boardA[1][0]==boardA[2][0] or boardA[0][1]==boardA[1][1]==boardA[2][1] or boardA[0][2]==boardA[1][2]==boardA[2][2]:
                validA=False
                pass
            if boardB[0][0]==boardB[0][1]==boardB[0][2] or boardB[1][0]==boardB[1][1]==boardB[1][2] or boardB[2][0]==boardB[2][1]==boardB[2][2]or boardB[1][1]==boardB[2][2]==boardB[0][0] or boardB[0][2]==boardB[1][1]==boardB[2][0]:
                validB=False
                pass
            if boardB[0][0]==boardB[1][0]==boardB[2][0] or boardB[0][1]==boardB[1][1]==boardB[2][1] or boardB[0][2]==boardB[1][2]==boardB[2][2]:
                validB=False
                pass
            if boardC[0][0]==boardC[0][1]==boardC[0][2] or boardC[1][0]==boardC[1][1]==boardC[1][2] or boardC[2][0]==boardC[2][1]==boardC[2][2] or boardC[1][1]==boardC[2][2]==boardC[0][0] or boardC[0][2]==boardC[1][1]==boardC[2][0]:
                validC=False
                pass 
            if boardC[0][0]==boardC[1][0]==boardC[2][0] or boardC[0][1]==boardC[1][1]==boardC[2][1] or boardC[0][2]==boardC[1][2]==boardC[2][2]:
                validC=False
                pass
            if validA==True and validB==True:
                print(*boardA[j],sep=" ",end="  ")
            if validA==True and validB==False and validC==False:
                print(*boardA[j],sep=" ")
            if validA==True and validB==False and validC==True:
                print(*boardA[j],sep=" ",end="  ")
            if validB==True and validC==True:
                print(*boardB[j],sep=" ",end="  ")
            if validB==True and validC==False:
                print(*boardB[j],sep=" ")
            if validC==True:
                print(*boardC[j],sep=" ")