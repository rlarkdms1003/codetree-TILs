#include <stdio.h>

int main() {
     int n, i;
     int cnt=0;
     for(i=0; i<5; i++) {
        scanf("%d\n", &n);
        if(n%2==0) {
            cnt++;
        }
     }
     printf("%d", cnt);

    return 0;
}