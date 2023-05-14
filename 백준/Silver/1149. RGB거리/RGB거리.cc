#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int price[1001][3];
int dp[1001][3];
int main(){
    int N;
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>price[i][0]>>price[i][1]>>price[i][2];
    }
    //dp[i][j]:i번째 집을 j로 칠했을때 최소비용
    //dp[i][0]=price[i][0]+dp[i-1][1], price[i][0]+dp[i-1][2]
    dp[1][0]=price[1][0];
    dp[1][1]=price[1][1];
    dp[1][2]=price[1][2];
    for(int i=2; i<=N; i++){
        dp[i][0]=min(dp[i-1][1]+price[i][0],dp[i-1][2]+price[i][0]);
        dp[i][1]=min(dp[i-1][0]+price[i][1],dp[i-1][2]+price[i][1]);
        dp[i][2]=min(dp[i-1][0]+price[i][2],dp[i-1][1]+price[i][2]);
    }
    cout<<min(dp[N][0],min(dp[N][1],dp[N][2]))<<'\n';
}