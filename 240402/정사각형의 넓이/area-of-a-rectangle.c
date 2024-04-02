#include <stdio.h>

int main() {
    int n, area;
    scanf("%d", &n);
    area = n*n;
    printf("%d", area);
    if (n < 5) {
        printf("tiny");
    }
    return 0;
}