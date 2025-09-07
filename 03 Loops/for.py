for i in range(20):
      print(i)

# 16 ->> 1
for i in range(16, 1, -1):
      print(i)

# -3 ->> -16
for i in range(-3, -16, -1):
      print(i)


# Lets print a table of 5
for i in range(5, 51, 5):
      print(i)

# Using taking input
n = int(input("which table you want: "))

for i in range(n, (n*10)+1, n):
      print(i)