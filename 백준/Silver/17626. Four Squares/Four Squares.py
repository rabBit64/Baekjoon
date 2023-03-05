N = int(input())
dp = [1e+8 for _ in range(50001)]
dp[0]=0
for i in range(1,int(N**(1/2))+1):
  dp[i**2]=1

for i in range(2,N+1):
  for j in range(1,int(i**(1/2))+1):
    dp[i]=min(dp[i],dp[i-(j**2)]+1)


print(dp[N])