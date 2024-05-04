#include <stdio.h>

int main() {
    int a, b, i;
    scanf("%d %d", &b, &a);
    while(a<=b) {
    printf("%d ", b);
    b-=2; 
    }
    return 0;
}