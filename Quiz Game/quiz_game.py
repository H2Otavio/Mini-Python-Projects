print("Hello, welcome to my computer quiz!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    print("Okay! See ya later!")
    quit()

print("Okay! Let's play a game :)")

result = 0

answer = input("What does CPU stands for?\n A: ")
if answer.lower() == 'central processing unit':
    print("Correct!")
    result += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stands for?\n A: ")
if answer.lower() == 'random access memory':
    print("Correct!")
    result += 1
else: 
    print("Incorrect!")

answer = input("What does GPU stands for?\n A: ")
if answer.lower() == 'graphics processing unit':
    print("Correct!")
    result += 1
else: 
    print("Incorrect!")

answer = input("What does PSU stands for?\n A: ")
if answer.lower() == 'power supply unit':
    print("Correct!")
    result += 1
else: 
    print("Incorrect!")

answer = input("What does HDD stands for?\n A: ")
if answer.lower() == 'hard drive disk':
    print("Correct!")
    result += 1
else: 
    print("Incorrect!")

print("You got "+str(result)+"/5 correct!" )