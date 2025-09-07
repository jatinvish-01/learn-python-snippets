# Break
for i in range(1, 21):
      if i == 15:
            break
      print(i)


# Continue
for i in range(1, 21):
      if i == 15:
            continue # skip 15
      print(i)


# Else
for i in range(1, 21):
      if i == 56:
            print("Break statement is executed")
            break
      print(i)
else:
      print("Break statement is not executed")

# Break run✅      Else run❌
# Break run❌      Else run✅