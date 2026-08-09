'''
Basic Rules:
1 = Snake 
-1 = Water
0 = Gun
'''
import random

computer =random.choice([-1,0,1])
user_input = input("Enter your choice: ")

user_input_dictionary ={"s" : 1 , "g" : 0 , "w" : -1}
reverse_dictionary={1:"Snake", 0:"Gun" , -1: "Water"}

user= user_input_dictionary[user_input]

print("-------- WELCOME TO WGS GAME --------")
print("--------GAME START--------")

print(f"You Chose: {reverse_dictionary[user]}\nComputer Chose: {reverse_dictionary[computer]}")

if(computer == user):
    print("It's a Draw")
else:
    if(computer==-1 and user ==0):  
        print("You Lose!")
    elif(computer==-1 and user ==1):  
        print("You Win!")
    elif(computer==1 and user ==-1): 
        print("You Lose!")
    elif(computer==1 and user ==0): 
        print("You Win!")
    elif(computer==0 and user ==1):  
        print("You Lose!")
    elif(computer==0 and user ==-1): 
        print("You Win!")
    else:
        print("Error 404")






