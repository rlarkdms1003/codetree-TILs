#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<2*n; i++) {
        if(i%2==1) {
            for(int j=0; j<(i/2)+1; j++) {
                printf("* ");
            }
        }
        else {
            for(int j=0; j<n-(i/2); j++) {
                printf("* ");
            }
        }
        printf("\n");
    }
    return 0;
}