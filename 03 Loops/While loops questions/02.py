# Accept a numeber and print its reverse 

a = int(input("Tell your num: "))
rev = 0

while a > 0:
      rev = rev * 10 + a % 10
      a = a // 10
print(rev)