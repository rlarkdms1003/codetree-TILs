#include <stdio.h>

int main() {
    int n;
    int m;
    scanf("%d", &m);
    int cnt=0;
    for(int i=0; i<m; i++) {
        scanf("%d", &n);
       }
    
    while(n !=1) {
        if(n%2==1) {
            n = n*3+1;
            
        }
        else
        n = n/2;
        cnt++;
    }
    printf("%d", cnt);
    return 0;
}