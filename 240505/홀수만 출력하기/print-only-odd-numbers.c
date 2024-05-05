#include <stdio.h>

int main() {
    int N, a, i;
    scanf("%d\n", &N);
    for(i= 1; i<=N; i++) {
        int i=a;
        scanf("%d\n", &a);
        if(a%2==1 && a%3==0) {
            printf("%d\n", a);
        }
    }
    return 0;
}