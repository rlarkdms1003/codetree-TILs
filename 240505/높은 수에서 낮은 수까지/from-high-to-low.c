#include <stdio.h>

int main() {
    int a, b,i;
    scanf("%d %d", &a, &b);
    if(b>=a) {
        for(i=b; i>=a; i--) {
            printf("%d ",b);
            b -=1;
        }
    }
    else {
        for(i=a; i>b; i--) {
            printf("%d ", a);
            a-=1;
        }
    }
    return 0;
}