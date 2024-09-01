#include <stdio.h>

int main() {
    int n=0;
    int sum=0;
    for(int i=0; i<10; i++) {
        scanf("%d", &n);
        sum +=n;
    }
    printf("%d", sum);
    return 0;
}