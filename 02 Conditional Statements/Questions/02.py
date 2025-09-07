"""Accept the gender from the user as char and print the 
respective greeting message 
Ex - Good Morning Sir (on the basis of gender)"""

a = str(input("Enter your gender: "))

if a == "male":
      print("Good morning Sir")
elif a == "female":
      print("Good morning Ma'am")
else:
      print("Have a nice day")