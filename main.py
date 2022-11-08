run = "python main.py"
# Unit 1 Guessing Game
# 1. Import the random module
# 2a. Create a boolean variable to indicate rounds of the game and a while loop using that boolean
# 2b. Create a variable that stores the result of input provided by the user, ask them to - "Type a number for an upper bound: "
# 3a. Check if a valid number was entered using an if statement
# 3b. If it is a valid number, print "Let's play!" and set the boolean variable to False
# 3c. "Scrub" the value of the entered number, by setting it to an int 
# 3d. Write the else condition and give the user an error message

# TEST IT OUT AND SEE WHAT HAPPENS WITH DIFFERENT INPUTS

# 4. Generate a random number from the range 1 to the number the user entered, make sure it is outside your while loop - known as a global variable
# 5. Create two more variables - one for the guess and one for the count of guesses 
# 6a. Create a new while loop below these variables that runs while the guess vairable is not equal to the random number
# 6b. Update the guess variable with input from the user, prompt them by saying "Type a number between 1 and" add the number they orginally entered
# 7. Verify the guess is a number (like before) and if it is, update the guess variable to be the value of itself as an int
# 8. Check it! Make an if else statement to see if guess equals the random number, if it does tell the user they won! If it does not, update the guess count number by 1
# 9. Let the user know how many guesses it took.  Print a message using the guess count number - make sure it makes sense no matter what the number is
# 10. Make the game playable more than once, add a while loop around all of your code

import random

boolean2=True
boolean=True
count=0

while boolean2:
  y=input("Choose a maximum number: ")
  if int(y) > 1 & y.isdigit() :
    number=random.randrange(1,int(y))
    boolean2=False
  else :
    print("It must a valid number greater than 1.")


while boolean:
  guess=input("Guess a number! ")
  if guess.isdigit():
    boolean=False
    guess=int(guess)
  else :
    print("Not a valid input. Try again!")
if guess==number :
  count=count+1
  print("Correct! You win!")
  print("Guess Count: " + str(count))
  print("\n")
if guess>number :
      guess=int(guess)
      count=count+1
      print("Guess lower")
if guess<number :
      guess=int(guess)
      count=count+1
      print("Guess higher")
  
else :
   count=count+1
while guess!=number:
  guess=input("Guess another number between 1 and " + str(y) + ": ")
  if guess.isdigit():
    guess=(int(guess))
    if guess == number :
      
      print("Correct! You win!")
      print("Guess Count: " + str(count))
      print("\n")      
    if int(guess)>number :
      guess=int(guess)
      count=count+1
      print("Guess lower")
    if int(guess)<number :
      guess=int(guess)
      count=count+1
      print("Guess higher")
  else :
    print("Not a valid number. Try again")