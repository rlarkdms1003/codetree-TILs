#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(i%2==0) {
                printf("%d ", (i/2)*(n*3)+1+j);
            }
            else {
                printf("%d ", (i/2)*(n*3)+(j+1)*2+n);
            }
        }
        printf("\n");
    }
    return 0;
}