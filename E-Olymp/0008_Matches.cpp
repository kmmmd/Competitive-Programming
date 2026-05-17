#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int n;
    cin>>n;
    int kok=pow(n,0.5);
    int s=2*kok*(kok+1);
    for (int i=0;i<(n-pow(kok,2));i++){
        if (i==0 || i==kok)
        s+=3;
        else
        s+=2;}
    cout<<s;
    return 0;}
