"""
Count all letters, digits, and special symbols from a given 
string 
Given: str1 = "P@#yn26at^&i5ve"

Using string methods 
"""

a = "hkufdklkjd57092910#%$&*#$^*#@"

digit = 0
char = 0
spchar = 0

for i in a:
      if i.isdigit():
            digit +=1
      elif i.isalpha():
            char +=1
      else:
            spchar +=1
print(f"Your digits are {digit}\n character is {char}\n and special character is {spchar}")