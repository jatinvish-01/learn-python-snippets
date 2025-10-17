n = int(input("Check your number is perfect or not: "))
sum = 0
for i in range(1, n):
      if n % i == 0:
            sum += i
if sum == n:
       print("Your number is perfect")
else:
      print("Your number is not perfect")