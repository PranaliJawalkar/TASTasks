import random
attempt=0
while(True):
    number=random.randint(0,100)
    #ask user do you want to play again
    if(attempt>0):
        again=input("Do you want to play again:yes or no\n")
        if(again=='no'):
            break
    while(True):
    #accepting a number from the user
        num=int(input("Guess the number:"))
        attempt+=1
    #check user number and random number are equal or not
        if(num==number):
            print("Congratulations you guess currect number\n")
            print(f"You take {attempt} number of attempts\n")
            break
        elif(num>number):
            print("Your number is greater than target number\n")
        elif(num<number):
            print("Your number is less than target number\n")
    
print("Thank you")