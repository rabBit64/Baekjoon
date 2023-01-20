'''
그리디
일단 정렬을 생각하자
종료시점에 대해 정렬

'''
n = int(input())
arr = []
for _ in range(n):
  start,end = map(int,input().split())
  arr.append((start,end))
arr.sort(key= lambda x:x[0])
arr.sort(key = lambda x:x[1])
count = 1
time = arr[0][1]
for i in range(1,n):
  if arr[i][0]>=time:
    time = arr[i][1]
    count+=1
print(count)
