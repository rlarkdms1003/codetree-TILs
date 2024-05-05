#include <stdio.h>

int main() {
    int n, i;
    int cnt=0;
    for(i=0; i<10; i++) {
        scanf("%d\n", &n);
        if(i%2==1) {
            cnt++;
        }
    }

    printf("%d", cnt);
    return 0;
}