compAnswer = 15
print("Do You wanna play with me?", "If Yes - write Y if Not write N")


userAnswer = input(str()) #Answer for Yes or No
if userAnswer is "Y":
    print("""Excellent! Let's Play""" + """Please tell me your name, It'll be easier to communicate :)""")
    userName = input(str())
    print("Hello " + userName + " So We can start now!")
elif userAnswer is "N":
    print("""Its so sad! See You next time!""")
else:
    print("You should write only Y or N")
    

print("I want to play with You in a simple game!")
print("Soouunddss nice " + userName + " ?")
print("""I'm just a simple machine, so U have a chance to beat me!""")
print("""Muahahhahaha""")
print("Try to guess, what number Im thinking about")
print("If You wanna little Hint - write Y, if Not - write No")

userAnswer2= input(str()) #Answer for Yes or No
if userAnswer2 is "Y":
  print(userName + " My number is somewhere in beetween 10 and 25. Guess What is my number?")
elif userAnswer2 is "N":
  print("Ok!, so what is my number?")
else:
  print("Please decide Y or N")
  
userFinalAnswer = int(input("Enter a number: "))
if userFinalAnswer >=  25:
 print("""It's too much""")
elif userFinalAnswer > 15 < 25:
  print("""You're closer!""")
elif userFinalAnswer == 15:
  print("Well done U Bastard!")
elif userFinalAnswer < 15 > 10:
  print("""You're so close! Keep trying! :)""")
elif userFinalAnswer  >= 1 < 10:
  print("A little bit more!")
else:
  print("""Ohhh I'll give U the hint, cause U're farrr farr awaaaaayyy""")
  
again = input("Wanna try again? Enter Y for Yes and N for NO")
if again is "N":
  print("Ok lets try again!")
elif again is "N":
     print("Thanks Bye!")
     
userFinalAnswer = int(input("Enter a number: "))
if userFinalAnswer >=  25:
 print("""It's too much""")
elif userFinalAnswer > 15 < 25:
  print("""You're closer!""")
elif userFinalAnswer == 15:
  print("Well done U Bastard!")
elif userFinalAnswer < 15 > 10:
  print("""You're so close! Keep trying! :)""")
elif userFinalAnswer  >= 1 < 10:
  print("A little bit more!")
else:
  print("""Ohhh I'll give U the hint, cause U're farrr farr awaaaaayyy""")


 
  
  
  
  

    
    
 
    
    
  

      
  
