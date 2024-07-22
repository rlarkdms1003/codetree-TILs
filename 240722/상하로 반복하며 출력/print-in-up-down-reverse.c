#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(j%2==0) {
                printf("%d", i+1);
            }
            if(j%2==1){
                printf("%d", n-i);
            }
           
        }
        printf("\n");
    }
    return 0;
}