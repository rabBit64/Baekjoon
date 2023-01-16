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
