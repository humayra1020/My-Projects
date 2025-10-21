#Simple quiz

print("Welcome to my computer quiz!")

play = input("do you want to play? (yes / no) :")
mark = 0

if play.lower() != "yes" :
    quit()

print("okay! let's play : )")

ans = input("what does CPU standfor? :")
if ans.lower() == "central processing unit" :
    print("Correct!")
    mark += 1
else:
    print("Incorrect!")
    

ans = input("what does ROM standfor? :")
if ans.lower() == "read only memory" :
    print("Correct!")
    mark += 1
else:
    print("Incorrect!")
    
ans = input("what does GPU stand for? :")
if ans.lower() == "graphics processing unit" :
    print("Correct!")
    mark += 1
else:
    print("Incorrect!")
    
    
ans = input("what does RAM standfor? :")
if ans.lower() == "random access memory" :
    print("Correct!")
    mark += 1
else:
    print("Incorrect!")
    
print("wallah! You have completed the quiz!")
print("Your score is :",mark)
print("You got "+str((mark/4)*100) + "%")

        
    
                
            
            