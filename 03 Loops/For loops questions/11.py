# Reverse string without using in build functions

a = "HAPPYCODING"  
b = ""

for i in range(len(a)-1, -1, -1):
      b = b + a[i]     
print(b)
