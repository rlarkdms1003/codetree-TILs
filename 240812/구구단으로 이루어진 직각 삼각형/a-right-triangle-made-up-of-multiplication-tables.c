#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        for(int j =1; j<=n-i+1; j++) {
            if(j<=n-i) {
                printf("%d * %d = %d / ", i, j, i*j);
            }
            else if(j==n-i+1) {
                printf("%d * %d = %d ", i, j, i*j);
                printf("\n");
            }
        }
    }
    return 0;
}