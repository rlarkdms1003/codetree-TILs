#include <stdio.h>

int main() {
    int a, b, i;
    scanf("%d %d", &a, &b);
    for(i=a; i<=b;) {
        if(i%2==1) {
            printf("%d ", i);
            i*=2;
        }
        else {
            printf("%d ", i);
            i+=3;
        }
    }
    return 0;
}