#include <iostream>
using namespace std;
void fun(int m){
    if (m>=0 && m<=9)
    cout<<"0"<<m;
    else
    cout<<m;}
int main(){
    int n,a,b,c;
    cin>>n;
    a=n%60;
    if (n/60>=60)
        b=(n-a)/60-((n-a)/3600)*60;
    else
    b=(n-a)/60;
    if (((n-a)/3600)>=24)
        c=(n-a)/3600-(((n-a)/3600)/24)*24;
    else
    c=(n-a)/3600;
    cout<<c<<":"; fun(b); cout<<":"; fun(a);
    return 0;}