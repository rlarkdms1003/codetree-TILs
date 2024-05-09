#include <stdio.h>

int main() {
    int n;
    int sum=0;
    int i;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        sum += i;
        if(n<=sum) {
            break;
        }
        
    }
    printf("%d", i);


    return 0;
}