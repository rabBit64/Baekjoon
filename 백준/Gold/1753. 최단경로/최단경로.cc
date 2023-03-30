#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

const int INF=0x7fffffff;
vector<pair<int,int>> graph[20001];

vector<int> dijkstra(int start){
    vector<int> dist(20001,INF);
    priority_queue<pair<int,int>> pq;
    pq.push({0,start}); //거리가 먼저와야함
    dist[start]=0;

    while(!pq.empty()){
        int cost=-pq.top().first;
        int cur=pq.top().second;
        //cout<<"현재노드는 "<<cur<<" 현재cost는 "<<cost<<endl;
        pq.pop();
        
        if(dist[cur]<cost) continue;//

        for(int i=0; i<graph[cur].size(); i++){
            if(cost+graph[cur][i].second<dist[graph[cur][i].first]){
                pq.push({-(cost+graph[cur][i].second), graph[cur][i].first});
                dist[graph[cur][i].first]=cost+graph[cur][i].second;
            }
        }
    }
    return dist;
}
/*
void dijkstra(int* dist,){

}
*/
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int V,E;
    cin>>V>>E;
    int K;
    cin>>K;
    for(int i=0; i<E; i++){
        int u,v,w;
        cin>>u>>v>>w;
        graph[u].push_back({v,w});
    }
    vector<int> answer=dijkstra(K);
    for(int i=1; i<=V; i++){
        //cout<<(answer[i]==INF)?"INF":answer[i])<'\n';
        if(answer[i]==INF){
            cout<<"INF"<<'\n';
        }else{
            cout<<answer[i]<<'\n';
        }
       
    }
}