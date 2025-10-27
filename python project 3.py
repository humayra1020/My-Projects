#Rock paper scissors game

import random

user_wnis = 0
computer_wins = 0
options =  ["rock","paper","scissors"]
while True:
    user_input = input("Types Rock/Paper/Scissors or Q to quit :").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_num = random.randint(0,2)
    #rock: 0, paper: 1, scissors: 2
    
    computer_pick = options[random_num]
    print("computer pick :",computer_pick)
    
    if user_input == "rock" and computer_pick == "scissors" :
        print("you win!")
        user_wnis += 1
        continue
    elif user_input == "paper" and computer_pick == "rock" :
        print("you win!")
        user_wnis += 1
    elif user_input == "scissors" and computer_pick == "paper" :
        print("you win!")
        user_wnis += 1
    else:
        print("you lost!")
        computer_wins += 1
        
print("You won ", user_wnis , " times")
print("computer won ", computer_wins," times")
    
        
print("Goodbye!")
        

    
