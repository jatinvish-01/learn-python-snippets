# Check the number is prime or not

n = int(input("Enter the number to check if it is prime or not: "))
is_prime = True
for i in range(1, n+1):
      if n % i == 0:
            is_prime = False
            break
if is_prime:
      print("The number is prime number")
else:
      print("Number is not a prime number")     