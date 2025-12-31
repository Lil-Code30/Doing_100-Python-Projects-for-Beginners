import random

print("Guess a number between 1 and 100.")

randomNumber = random.randint(1, 100)
userGuess = None

print(randomNumber)
print(userGuess)
print("===========")

while(userGuess != randomNumber):
    print("Input values:")
    userGuess = int(input("Enter your guess: "))
    
    print("Output value: ")
    if(userGuess < randomNumber):
        print("Too low! Try again.")     
    elif (userGuess > randomNumber):
        print("Too high! Try again.")      

print("Correct! You guessed the number.")