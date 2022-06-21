isHungry = input("Are you hungry?(y/n) ")
isBored = input("Are you bored?(y/n) ")


if (isHungry == "y" or isHungry == "Y"):
  print("Go eat")
else:
  print("Don't eat")

if (isBored == "y" or isBored == "Y"):
  print("Go to sleep")
else:
  print("Go exercise") 

userNumber = int(input("Enter a whole number: "))

if (userNumber >=0):
  print("Your number is a positive number")
else:
  print("Your number is a negative number")

userAge = int(input("Enter you age: ")) 

# asks the user for their age and tell the user what movie they can watch based on their age
if (userAge > 17):
  print("You can watch any movie")
elif (userAge < 17 and userAge >13):
  print("You can watch g-rated and pg-13 movies")
else:
  print("you can only watch g-rated movies")
