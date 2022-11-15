run = "python main.py"

# Unit 1 Guessing Game

import random

boolean2=True
boolean=True
boolean3=True
player2boolean=True
count1=0
count2=0
wholeGameLoop=True
again=""
boolean4=True

while wholeGameLoop:
  while boolean2:
    player1=input("Player 1, insert your name: ")
    x=input(str(player1)+" : Choose a minimum number: ")
    if  x.isdigit() :
        boolean3=False
    player2=input("Player 2, insert your name: ")
    y=input(str(player2)+" : Choose a maximum number: ")
    if  y.isdigit() :
      if int(y) > int(x) :
        number=random.randrange(int(x),int(y))
        boolean2=False
      else :
        print("At least one input was invalid. The minimum must be a whole number less than the maximum")
    else :
      print("At least one input was invalid. The minimum must be a whole number less than the maximum")
  
  
  while boolean:
    guess=input(str(player1) +": Guess a number between " + str(x)+ " and " + str(y) + ": ")
    if guess.isdigit():
      boolean=False
      guess=int(guess)
    else :
      print("Not a valid input. Try again!")
  if guess==number :
    count1=count1+1
    print("Correct! "+ str(player1) + " wins!")
    print("Guess Count: " + str(count1))
    print("\n")
  if guess>number :
        guess=int(guess)
        count1=count1+1
        print("Guess lower")
  if guess<number :
        guess=int(guess)
        count1=count1+1
        print("Guess higher")
  
  if guess!=number :
    while player2boolean:
      guess=input(str(player2) + ": Guess another number between " + str(x)+ " and " + str(y) + ": ")
      if guess.isdigit():
        player2boolean=False
        guess=int(guess)
      else :
         print("Not a valid input. Try again!")
      if guess==number :
        count2=count2+1
        print("Correct! " + str(player2) + " wins!")
        print("Guess Count: " + str(count2))
        print("\n")
      if guess>number :
            guess=int(guess)
            count2=count2+1
            print("Guess lower")
      if guess<number :
            guess=int(guess)
            count2=count2+1
            print("Guess higher")
      
  while guess!=number:
    guess=input(str(player1) + ": Guess another number between " + str(x)+ " and " + str(y) + ": ")
    if guess.isdigit() :
      guess=(int(guess))
      if guess == number :
        count1+=1
        print("Correct! "+str(player1) +" wins!")
        print(str(player1) + " Guess Count: " + str(count1))
        print(str(player2) + " Guess Count: " + str(count2))
        print("\n")      
      if int(guess)>number :
        guess=int(guess)
        count1=count1+1
        print("Guess lower")
      if int(guess)<number :
        guess=int(guess)
        count1=count1+1
        print("Guess higher")
    else :
      print("Not a valid number. Try again")
    if guess!=number :
      guess=input(str(player2)+" Guess another number between " + str(x)+ " and " + str(y) + ": ")
      if guess.isdigit():
        guess=(int(guess))
        if guess == number :
          count2+=1
          print("Correct! "+str(player2) +" wins!")
          print(str(player1) + " Guess Count: " + str(count1))
          print(str(player2) + " Guess Count: " + str(count2))
          print("\n")      
        if int(guess)>number :
          guess=int(guess)
          count2=count2+1
          print("Guess lower")
        if int(guess)<number :
          guess=int(guess)
          count2=count2+1
          print("Guess higher")
      else :
        print("Not a valid number. Try again")
  again=input("Would you like to play again? Type y for yes and n for no: ")
  while boolean4 :
    if again=="y" :
      wholeGameLoop=True
      boolean4=False
    elif again=="n" :
      wholeGameLoop=False
      print("Thanks for playing!")
      boolean4=False
    else:
      print("Invalid input")
  
  boolean2=True
  boolean=True
  boolean3=True
  player2boolean=True
  count1=0
  count2=0
  boolean4=True