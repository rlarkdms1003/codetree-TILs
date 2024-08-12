#include <stdio.h>

int main() {
    int n;
    int sum_val = 1;
    int a, b;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d %d", &a, &b);
        int sum_mul = 1;
        
        for(int j=b; j>=a; j--) {
            int mul =j;
            sum_mul *= j;
        }
        printf("%d\n", sum_mul);
    }
    return 0;
}