'''
일단 n의 범위가 0을 포함한다는거에 주의하자
그리고 옷의 이름은 문제푸는데 필요없으니 버리자
착용해도 되고/안해도 되고
모두 다 착용안해도 되니까 -1'''
T = int(input())
for _ in range(T):
  n = int(input())
  dict = {}
  for _ in range(n):
    a = list(input().split())
    if a[1] in dict:
      dict[a[1]].append(a[0])
    else:
      dict[a[1]]=[a[0]] #이렇게 써줘야 에러 안남!@ㅡAttributeError: 'str' object has no attribute 'append'
  mul = 1
  for key in dict:
    mul *= (len(dict[key])+1)
  print(mul-1)
'''
from collections import defaultdict
T = int(input())
for _ in range(T):
  dict = defaultdict(list)
  n = int(input())
  for _ in range(n):
    a,b = input().split()
    dict[b].append(a)
  arr = []
  items = 0
  for key in dict:
    tmp = 0
    for item in dict[key]:
      items+=1
      tmp+=1
    arr.append(tmp)

  if len(dict)==1:
    print(items)
  elif len(dict)==0:
    print(0)
  else:
    mul = 1
    for a in arr:
      mul*=a
    print(mul+items)
    '''