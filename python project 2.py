#Number guessing game

import random
print ("Welcome to guessing number game!!")
ran = input("Type a number as a range from 0 to that number :")

if ran.isdigit():
    ran = int(ran)
    
    if ran <= 0 :
        print("Enter a number larger than 0 next time.")
        quit()
        
else:
    print("please type a valid number next time")
    quit()
        
num = random.randint(1,ran )
        
tries = 0   
while True :
    guess_num = input("Guess the random number :")
    tries += 1
    if guess_num.isdigit():
      guess_num = int(guess_num)
      if guess_num <= 0 :
          print("Enter a number larger than 0 next time.")
          quit()
        
    else:
        print("please type a valid number next time")
        quit()
    
    if guess_num == num :
        print("yeappii you got it!!")
        break
    elif guess_num < num :
        print("you are below the number")
    else:
        print("ypur above the num")
        
print("The number of tries :",tries)
    

    
    



