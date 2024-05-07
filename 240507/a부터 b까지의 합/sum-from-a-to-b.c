#include <stdio.h>

int main() {
    int a, b, i;
    int sum_val=0;
    scanf("%d %d", &a, &b);
    for(i=a; i<=b; i++) {
        sum_val+=i;
    }
    printf("%d", sum_val);
    return 0;
}