#include <iostream> //System failure
using namespace std;
int main(){
    int m,n;
    cin>>m>>n;
    int matrx[m][n];
    for(int i=0;i<m;i++)
    for(int j=0;j<n;j++)
    cin>>matrx[i][j];
    for(int i=m-1;i>0;i--)
    for(int j=0;j<n;j++){
        if (matrx[i-1][j]>matrx[i][j+1])
        cout<<"F";
        else
        cout<<"R";}
    return 0;}
