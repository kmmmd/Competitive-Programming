#include <iostream>
using namespace std;
int main(){
    int a,b,n;
    cin>>a>>b>>n;
    int ma=a*n+(b*n)/100,mb=b*n-((b*n)/100)*100;
    cout<<ma<<" "<<mb;
    return 0;}
