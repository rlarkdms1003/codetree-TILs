#include <stdio.h>

int main() {
    int a,b;
    scanf("%d %d", &a, &b);
    for(a, b; a<=b && b>=2; --a, --b) {
        printf("%d ", b, a);
    }
    return 0;
}