#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    int a;
    cin>>a;
    string b=to_string(a);
    reverse(b.begin(),b.end());
    if (to_string(a)==b)
    cout<<1;
    else cout<<37;
    return 0;}