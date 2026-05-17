#include <iostream>
using namespace std;
int main() {
    int a,b,c,s=0;
    cin>>a>>b>>c;
    if (a%2==1)
    s+=a/2+1;
    else
    s+=a/2;
    if (b%2==1)
    s+=b/2+1;
    else
    s+=b/2;
    if (c%2==1)
    s+=c/2+1;
    else
    s+=c/2;
    cout<<s;
    return 0;}
