counter=0
sum=0
while (sum<100):
    print("Enter player 1:")
    p1=int(input())     
    
    if (1<=p1<=10 ):
     
      counter=counter+1
    else:
          print("try again")
          p1=int(input())
    print("Enter player 2:")
    p2=int(input())   
    if (1<=p2<=10 ):
     
        counter=counter+1
    else:
          print("try again")
          p2=int(input())   
    sum=sum+p1+p2      
if (counter%2==0):
    print("player2 wins")
else:
    
    print("player1 wins")
    
