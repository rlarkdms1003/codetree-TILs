#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    n=n*2;
    for(int i=0; i<n; i+=2) {
        for(int j=0; j<=i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}