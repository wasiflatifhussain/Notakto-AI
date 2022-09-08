

def firstLine():  #this is printing the first line of the output
    from main import boardA,boardB,boardC
    # from main import moveStorer1stMove
    firstLine1=['A','B','C']
    if boardA[1][1]==boardA[2][2]==boardA[0][0] or boardA[0][2]==boardA[1][1]==boardA[2][0] and 'A' in firstLine1:
        if 'A' in firstLine1:
            firstLine1.remove('A')
    if boardA[0][0]==boardA[1][0]==boardA[2][0] or boardA[0][1]==boardA[1][1]==boardA[2][1] or boardA[0][2]==boardA[1][2]==boardA[2][2]:
        if 'A' in firstLine1:
            firstLine1.remove('A')
    if boardA[0][0]==boardA[0][1]==boardA[0][2] or boardA[1][0]==boardA[1][1]==boardA[1][2] or boardA[2][0]==boardA[2][1]==boardA[2][2] and 'A' in firstLine1:
        if 'A' in firstLine1:
            firstLine1.remove('A')
    if boardB[1][1]==boardB[2][2]==boardB[0][0] or boardB[0][2]==boardB[1][1]==boardB[2][0] and 'B' in firstLine1:
        if 'B' in firstLine1:
            firstLine1.remove('B')
    if boardB[0][0]==boardB[1][0]==boardB[2][0] or boardB[0][1]==boardB[1][1]==boardB[2][1] or boardB[0][2]==boardB[1][2]==boardB[2][2] and 'B' in firstLine1:
        if 'B' in firstLine1:
            firstLine1.remove('B')
    if boardB[0][0]==boardB[0][1]==boardB[0][2] or boardB[1][0]==boardB[1][1]==boardB[1][2] or boardB[2][0]==boardB[2][1]==boardB[2][2] and 'B' in firstLine1:
        if 'B' in firstLine1:
            firstLine1.remove('B')
    if boardC[1][1]==boardC[2][2]==boardC[0][0] or boardC[0][2]==boardC[1][1]==boardC[2][0] and 'C' in firstLine1:
        if 'C' in firstLine1:
            firstLine1.remove('C')
    if boardC[0][0]==boardC[1][0]==boardC[2][0] or boardC[0][1]==boardC[1][1]==boardC[2][1] or boardC[0][2]==boardC[1][2]==boardC[2][2] and 'C' in firstLine1:
        if 'C' in firstLine1:
            firstLine1.remove('C')
    if boardC[0][0]==boardC[0][1]==boardC[0][2] or boardC[1][0]==boardC[1][1]==boardC[1][2] or boardC[2][0]==boardC[2][1]==boardC[2][2] and 'C' in firstLine1:
        if 'C' in firstLine1:
            firstLine1.remove('C')
    a=len(firstLine1)
    if len(firstLine1)>0:
        return ("      ".join(firstLine1))