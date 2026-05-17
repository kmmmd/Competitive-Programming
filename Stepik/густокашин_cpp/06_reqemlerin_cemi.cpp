#include <iostream>
using namespace std;
int main() {
    int a,s=0;
    cin>>a;
    while (a>0){
        s+=(a%10);
        a/=10;}
    cout<<s;
    return 0;}
