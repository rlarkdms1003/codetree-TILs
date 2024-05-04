#include <stdio.h>

int main() {
    int a, b, i;
    scanf("%d %d", &a, &b);
    printf("%d.", a/b);
    
    a %=b;
    for(i=0; i<20; i++) {

        a *= 10;
        printf("%d", a/b);

        a %=b;
    }
    return 0;
}