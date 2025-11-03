# Check if string is pallindrome for not usinf function

def pallindrome(st):
      rev = ""
      for i in range(len(st)-1, -1, -1):
            rev = rev + st[i]

      if rev == st:
            print(f"{st}, is a Pallindrome")
      else:
            print(f"{st}, is Not a pallindrome")
                  
pallindrome(st = str(input("Enter the string: ")))