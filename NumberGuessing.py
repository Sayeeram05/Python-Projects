import random   # Used this library to generate random number

print('''\n----------- Lets play number Guessing game ! ----------- 
    \n\n
    How to Play ?
        1.Progarm will generate a random number 1 - 10
        2.You have to guess that number\n''')

RandomNumber = random.randint(0,10)  # Stores a random number
Attempts  = 1

while True:
    try :   # To handle the run time error
        UserGuessed = int(input("\nEnter the Number : "))
        if(UserGuessed < 0):
            print("Enter Number Greater Than 0")
        elif(UserGuessed == RandomNumber):
            print(f"Awesome You Gussed Correct In {Attempts} Attempts")
            break
        else:
            print("\nWrong Guess\n")
            Attempts += 1

    except Exception as e  :    # Shows the runtime error
        print(e,": Enter Correct Number")

    
    
