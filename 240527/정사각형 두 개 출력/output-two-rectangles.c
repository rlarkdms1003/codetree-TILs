#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            printf("*");
        }
        printf("\n");
    }
    printf("\n");

    for(int i=0; i<n; i++) {
        for(int l=0; l<n; l++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}