#include <stdio.h>

int main() {
    int n;
    int prod=1;
    int x = 0;
    scanf("%d", &n);
    while(1) {
        if(n==prod)
        break;

        prod *= 2;
        x++;
    }
    printf("%d", x);
    return 0;
}