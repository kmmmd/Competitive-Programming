#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n,m,l,r;
    scanf("%d",&n);
    vector<int>a(n+1);
    vector<int>s(n+1);
    for(int i=1;i<n+1;i++){
        scanf("%d",&a[i]);
        s[i]=s[i-1]+a[i];}
    scanf("%d",&m);
    vector<int>netice(m);
    for(int i=0;i<m;i++){
        scanf("%d %d",&l,&r);
        netice[i]=s[r]-s[l-1];}
    for(int i : netice){
    printf("%d",i);
    printf("\n");}
    return 0;} 
