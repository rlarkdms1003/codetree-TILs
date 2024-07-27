#include <stdio.h>

int main() {
    int a, b;
    scanf("%d%d", &a, &b);
            for(int j=a; j<10 ; j+=2) {
             for(int i=b; i>=a; i--) {
                if(j%2==0) {
            printf("%d * %d = %d", i, j, i*j);
            if(i!=2) {
                printf(" / ");
            }
                }
        }
         printf("\n");
    }
    return 0;
}