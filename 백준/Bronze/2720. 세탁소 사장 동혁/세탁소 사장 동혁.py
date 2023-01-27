def remain(C):
  print(C//25,(C%25)//10,((C%25)%10)//5,(((C%25)%10)%5))

T = int(input())
for _ in range(T):
  C = int(input())
  remain(C)