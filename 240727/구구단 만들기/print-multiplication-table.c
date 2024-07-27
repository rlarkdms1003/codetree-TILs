#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    if(b%2==0 && b!=a) {
            for(int j=1; j<10; j++) {
                for(int i=b; i>1; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>2) {
                printf(" / ");
            }
        }
        printf("\n");
    }
    }   
    else if(a!=b && b%2==1) {
            for(int j=1; j<10; j++) {
                for(int i=b-1; i>1; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>2) {
                    printf(" / ");}
            }
            printf("\n");
        }
    }
    if(a==b && b%2==0) {
            for(int i=1; i<10; i++) {
            printf("%d * %d = %d", a, i, a*i);
            printf("\n");
            }
        }
    return 0;
}