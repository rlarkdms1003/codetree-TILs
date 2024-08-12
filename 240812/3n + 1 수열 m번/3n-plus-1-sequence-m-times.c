#include <stdio.h>

int main() {
    int n;
    int m;
    scanf("%d", &m);

    for(int i=0; i<m; i++) {
        scanf("%d", &n);
        int cnt=0;
        while(n !=1) {
        if(n%2==1) {
            n = n*3+1;
            
        }
        else 
        n = n/=2;

        cnt++;
    }
    printf("%d\n", cnt);
    }
    
    return 0;
}