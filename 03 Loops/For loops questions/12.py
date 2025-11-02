# Check string pallindrome for not 

a = "NAMAN"  
b = ""

for i in range(len(a)-1, -1, -1):
      b = b + a[i] 
         
if b == a:
      print("Your string is pallindorme")
else:
      print("Its not a pallindrome")