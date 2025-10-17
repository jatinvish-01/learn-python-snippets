# Print the sum of all even & odd numbers in range separately.

n = int(input("Enter your number: "))
even = 0
odd = 0
for i in range(1, n+1):
      if i%2 == 0:
            even = even + i
      else:
            odd = odd + i 
print(f"Your sum of even or odd number {even}, {odd}")      