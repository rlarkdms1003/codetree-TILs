#include <stdio.h>

int main() {
    int n, i;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        if(i%3==0 || i%10==3 || i%10==6 || i%10==9) {
            printf("0 ");
        }
        else {
            printf("%d ", i);
        }
    }
    return 0;
}