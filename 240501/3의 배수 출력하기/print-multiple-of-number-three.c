#include <stdio.h>

int main() {
    int n,i=0;
    scanf("%d",&n);
    while(i<n) {
        if(i%3==0) {
            i+=3;
            printf("%d ", i);

        }

    }
    return 0;
}