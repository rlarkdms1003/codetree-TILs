#include <stdio.h>

int main() {
    int n, i;
    int sum_val=0;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        int a;
        scanf("%d/n", &a);
        if(a%2==1 && a%3==0) {
            sum_val +=a;
        }
    }
    printf("%d", sum_val);
    return 0;
}