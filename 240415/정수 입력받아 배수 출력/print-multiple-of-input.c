#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=n; i<=5*n; i+=n) {
        printf("%d ", i);
    }

    return 0;
}