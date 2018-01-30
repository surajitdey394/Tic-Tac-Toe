#tic tac toe
import random
import sys
board=[0,1,2,
       3,4,5,
       6,7,8]
def show():
    print (board[0],'|', board[1],'|' ,board[2])
    print('-----------')
    print (board[3],'|', board[4],'|' ,board[5])
    print('-----------')
    print (board[6],'|', board[7],'|' ,board[8])
    
'''def checkLine(char,spot1,spot2,spot3):
    if(board[spot1]==char and board[spot2]==char and board[spot3]==char):
        return True
def checkAll(char):
        if checkLine(char,0,1,2):
            True
        if checkLine(char,1,4,7):
            True
        if checkLine(char,2,5,8):
            True
        if checkLine(char,3,4,5):
            True
        if checkLine(char,6,7,8):
            True
        if checkLine(char,0,3,6):
            True
        if checkLine(char,2,4,6):
            True
        if checkLine(char,0,4,8):
            True
'''

def checkAll(char):
    lines = ["012","345","678","036","147","258","048","642"]
    match = char * 3 
    for line in lines:
      
        check = str(board[int(line[0])]) + str(board[int(line[1])]) + str(board[int(line[2])])
        if check == match:
            return True
            break 
 
show()
 

            
while True:
    a=int(input("select a spot: "))
   
    if board[a]!='x' and board[a]!='o':
        board[a]='x'

        if checkAll('x')==True:
            show()
            print("~~~X Wins~~~")
            
            
            break
    else:  

        print("this position is occupied")
        
    while True:
        random.seed()
        opponent=random.randint(0,8)
        if board[opponent]!='o' and board[opponent]!='x':
            board[opponent]='o'
            
            if checkAll('o')==True:
                print("~~~ O Wins~~~")
                show()
                
                break
                    
            break
            
    else:
        print("this position is occupied")
    
    show()
