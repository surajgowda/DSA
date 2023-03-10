                                                                   #x
ls = [['N','L','M','F','N','U','B','O','C','A','F','E','V','F','D'],#1
     ['U','J','S','M','B','O','T','L','L','U','E','Y','C','K','Y'], #2
     ['O','A','V','C','P','O','E','B','N','N','D','A','V','B','G'], #3
     ['T','F','S','N','S','H','S','I','B','B','U','R','S','B','D'], #4
     ['S','K','F','M','I','T','V','J','R','S','H','G','N','G','G'], #5
     ['J','I','R','E','P','E','T','J','E','K','W','I','K','G','Y'], #6
     ['U','L','A','S','R','W','H','E','E','L','P','K','B','E','F'], #7
     ['N','L','M','S','U','E','G','B','N','M','C','B','O','T','Y'], #8
     ['G','H','E','A','T','U','I','A','W','O','P','R','P','C','H'], #9
     ['R','W','W','G','F','S','L','R','L','L','B','I','I','T','T'], #10
     ['A','L','O','E','T','S','I','N','R','E','U','H','I','C','V'], #11
     ['R','K','R','A','P','I','W','A','J','A','L','G','S','N','E'], #12
     ['P','W','K','N','A','B','N','K','M','O','C','C','E','B','F'], #13
     ['I','M','J','G','J','W','U','R','A','F','W','D','V','K','K'], #14
     ['B','M','K','F','A','D','F','E','I','L','E','B','P','F','A']] #15
#y:    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15

words=['PARK','LIGHT','BANK','BELIEF','CARRIER','CAUSE','CIRCLE','FRAMEWORK','ISSUE','MESSAGE','OFFER','REFUGEE','RUBBISH','UNIVERSE','WHEEL']

# ---------------------------------------------------------------------------------
# DON'T TOUCH THE CODE BELOW
# ---------------------------------------------------------------------------------
def find(word):
    flag = 0
    for x in range(15):
        for y in range(16-len(word)):
            i=0
            for i in range(len(word)):
                if ls[x][y+i]==word[i]:
                    flag=1
                else:
                    flag=0
                    break
            if flag == 1:
                print(word,":H-",x+1,y+1)

    for x in range(16-len(word)):
        for y in range(15):
            i=0
            for i in range(len(word)):
                if ls[x+i][y]==word[i]:
                    flag=1
                else:
                    flag=0
                    break
            if flag == 1:
                print(word,":V-",x+1,y+1)

    for x in range(15):
        for y in range(14,0+len(word)-1,-1):
            i=0
            for i in range(len(word)):
                if ls[x][y-i]==word[i]:
                    flag=1
                else:
                    flag=0
                    break
            if flag == 1:
                print(word,":Ulta H-",x+1,y+1)

    for x in range(14,0+len(word)-1,-1):
        for y in range(15):
            i=0
            for i in range(len(word)):
                if ls[x-i][y]==word[i]:
                    flag=1
                else:
                    flag=0
                    break
            if flag == 1:
                print(word,":Ulta V-",x+1,y+1)
    print("----------------------------------------------------------------")

for word in words:
    find(word)
