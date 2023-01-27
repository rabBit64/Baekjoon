#10101
arr = [int(input()) for _ in range(3)] #이렇게 한줄로
if all(a==60 for a in arr):#all 함수
    print('Equilateral')
elif (s:=sum(arr)==180) and len(set(arr))==2:
    print('Isosceles')
elif s:
    print('Scalene')
else:
  print('Error')