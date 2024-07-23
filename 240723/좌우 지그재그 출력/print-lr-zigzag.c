#include <stdio.h>

int main() {
    int n;
    int cnt=0;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(i%2==0) {
                printf("%d ", i*n+j+1);
            }
            if(i%2==1) {
                printf("%d ", (i*n)+n-j);
            }
           
        }
        printf("\n");
    }
    return 0;
}