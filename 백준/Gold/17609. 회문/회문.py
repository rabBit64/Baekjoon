import sys

def palindrome(str):
  if str==str[::-1]:
    return 0
  else:
    i, j = 0, len(str)-1
    while i<j:
      if str[i]==str[j]:
        i+=1
        j-=1
      else:
        str2 = str[:i]+str[i+1:]
        str3 = str[:j]+str[j+1:]
        if str2==str2[::-1] or str3==str3[::-1]:
          return 1
        else:
          return 2

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
  str = sys.stdin.readline().rstrip()
  print(palindrome(str))