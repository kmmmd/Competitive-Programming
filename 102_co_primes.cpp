#include <iostream>
using namespace std;
int ebob(int m,int n){
    while (m!=n){
        if (m>n)
        m=m-n;
        else
        n=n-m;}
    return m;}
int main(){
    int a,say=0;
    cin>>a;
    for (int i=1;i<a;i++){
        if (ebob(a,i)==1)
        say++;}
    cout<<say;
    return 0;}