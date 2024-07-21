#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    for(int i=1; i<5; i++) {
        for(int j=1; j<6; j++) {
            printf("%d ", i*j);
        }
        printf("\n");
    }
    return 0;
}