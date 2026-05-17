#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int v,s=109,t;
    cin>>v>>t;
    int hasil=v*t;
    if (t==0)
    cout<<0;
    else if(hasil>s)
    cout<<(hasil-s*(hasil/s));
    else{
        if (abs(hasil)>s){
            if (abs(hasil)%s==0) cout<<0;
            else cout<<(s-(abs(hasil)-s*(abs(hasil)/s)));}
        else
        cout<<(s-abs(hasil));}
    return 0;}