# Accept name and age from the user. Check if the user is a valid voter or not.

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age < 18:
      print(f"Hello {name} you not able to vote")
else:
      print(f"Hello {name} you valid to voting")