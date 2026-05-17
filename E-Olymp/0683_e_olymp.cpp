//vaxt limiti asir
#include <stdio.h> 
#include <string.h>
using namespace std;
int main(void) {
    int i, j, n, m, value; 
    int mas[1000][1000]; 
    scanf("%d %d",&n,&m);
    for(i = 1; i <= n; i++)
    for(j = 1; j <= m; j++){
        scanf("%d",&value); 
        mas[i][j] = mas[i][j-1] + mas[i-1][j] - mas[i-1][j-1] + value;}
    for(i=1; i <= n; i++){
    for(j=1; j <= m; j++){
        printf("%d ",mas[i][j]);}
        printf("\n");}
    return 0; } 
