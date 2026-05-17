#include <iostream>
#include <cstring>
using namespace std;
int main() {
    char a[1000];
    cin>>a;
    if (strlen(a)==1)
    cout<<0;
    else
    cout<<a[strlen(a)-2];
    return 0;}
