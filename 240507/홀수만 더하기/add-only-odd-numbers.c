#include <stdio.h>

int main() {
    int n, i;
    int sum_val=0;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        scanf("%d/n", &n);
        if(n%2==1 && n%3==0) {
            sum_val += n;
        }
    }
    printf("%d", sum_val);
    return 0;
}