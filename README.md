# baekjoon



##### 파이썬 풀면서 느낀 이모저모.. 👼🏻
```
import sys
sys.stdin.readline() # 이게 더 빠름!
```
```
import sys
input = sys.stdin.readline
int(input().rstrip()) #readline으로 입력받으면 개행 들어가서 rstrip 써줘야
```
```
arr = [list(input().rstrip()) for _ in range(n)] # 이렇게 띄어쓰기 없을때 입력받기!
```
```
arr[row][col],arr[nrow][ncol] = arr[nrow][ncol],arr[row][col] # 이렇게 바로 swap이 되는구나..
```
-띄어쓰기 없는 이차원배열 입력받기
```
arr = [list(map(int,input().strip())) for _ in range(n)]
```
-파이썬 string 함수들 활용..
```
str.cnt('a')
str.replace(i,'*')
str.find(chr(i))
// join은 문자열 함수임!
구분자.join(문자열리스트)
```
아스키코드로 'a'는 97 (~122) 'A'는 65 (~90)
- set의 원소삭제는 ```s.remove(원소)```
