'''
일단 dp임.
부분수열에 대한 길이를 채워나간다..
LCS(Xi,Yj): LCS(Xi-1,Yj-1)+1  if(Xi==Yj)
LCS(Xi,Yj): max(LCS(Xi-1,Yj),LCS(Xi,Yj-1))  if(Xi != Yj)
'''
import sys
input = sys.stdin.readline
word1,word2 = input().strip(), input().strip()
dp = [[0]* (len(word2)+1) for _ in range(len(word1)+1)]

for i in range(1,len(word1)+1):
  for j in range(1,len(word2)+1):
    if word1[i-1] == word2[j-1]:
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])