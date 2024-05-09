#include <stdio.h>

int main() {
    int n, i;
    int sum=1;
    scanf("%d", &n);
    for(i=1; i<=10; i++) {
        sum *= i;
        if(sum>=n) {
            break;
        }
    
    }
    printf("%d", i);
    return 0;
}