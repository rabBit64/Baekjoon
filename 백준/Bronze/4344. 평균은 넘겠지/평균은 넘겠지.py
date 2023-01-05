C = input()
for i in range(int(C)):
  arr = list(map(int,input().split()))
  '''
  num = arr[0]
  arr.pop(0)
  sum = 0
  for items in arr:
    sum+=items
  avg = sum/num
  '''
  avg = sum(arr[1:])/arr[0]

  cnt2 = 0
  for items in arr[1:]:
    if items>avg:
      cnt2+=1
  rate = (cnt2/arr[0])*100
  print(f'{rate:.3f}%')