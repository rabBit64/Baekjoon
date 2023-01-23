#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int main(){
    int n;
    long long tmp;
    vector<long long> x1;
    vector<long long> x2;
    cin>>n;
    for(int i=0; i<n; i++){
        cin>>tmp;
        x1.push_back(tmp);
        x2.push_back(tmp);
    }
    sort(x1.begin(),x1.end());
    x1.erase(unique(x1.begin(),x1.end()),x1.end());
    for(int i=0; i<n; i++){
        cout<<lower_bound(x1.begin(),x1.end(),x2[i])-x1.begin()<<" ";
    }
}