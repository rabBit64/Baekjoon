import sys
n,m=map(int,input().split())
nameList = sys.stdin.read().splitlines()
heard =set(nameList[:n])
seen= set(nameList[n:])
heardSeen = list(heard & seen)
print(len(heardSeen))
for name in sorted(heardSeen):
  print(name)