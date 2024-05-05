#include <stdio.h>

int main() {
    int N, a, i;
    scanf("%d\n", &N);
    for(i= 1; i<=N; i++) {
        int i=a;
        scanf("%d\n", &a);
        if(i%2==1 && i%3==0) {
            printf("%d\n", i);
        }
    }
    return 0;
}