N = input()

#자리수
length = len(N)
cnt = 0
a = 1
b = 9
for i in range(1,length):
  cnt+=(i)* (b-a+1)
  a *= 10
  new_b =''
  for j in range(i+1):
    new_b+='9'
  b = int(new_b)

print(cnt+(int(N)-(10 ** (length-1))+1)*length)