#include <iostream>
using namespace std;
int main(){
    int h,a,b,s=0,gun=1;
    cin>>h>>a>>b;
    while((s+a)<h){
        s=(s+a)-b; gun++;}
    cout<<gun;
    return 0;}