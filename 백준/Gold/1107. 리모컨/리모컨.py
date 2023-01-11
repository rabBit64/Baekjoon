'''
풀면서 찾은거..
set은 in 을 쓰자
선언은 s = set()
d = {} 이건 딕셔너리이고
'''
import sys
input = sys.stdin.readline

channel = int(input())
M = int(input())
if M:
  broke = set(input().rstrip().split())
else:
  broke = set()
cnt = abs(100-channel)

for k in range(1000001):
  num = str(k)
  for i in range(len(num)):
    if num[i] in broke:
      break
    if i==len(num)-1:
      cnt = min(cnt,abs(channel-k)+len(num))
print(cnt)

