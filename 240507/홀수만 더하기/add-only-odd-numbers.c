#include <stdio.h>

int main() {
    int n, N, i;
    int sum_val=0;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        scanf("%d/n", &n);
        if(N%2==1 && N%3==0) {
            sum_val += N;
        }
    }
    printf("%d", sum_val);
    return 0;
}