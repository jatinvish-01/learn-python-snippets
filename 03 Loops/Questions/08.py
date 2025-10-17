# Print all the factors of the numbers

n = int(input("Enter a number: "))
for i in range(1, n + 1):
      if n % i == 0:
            print(i)