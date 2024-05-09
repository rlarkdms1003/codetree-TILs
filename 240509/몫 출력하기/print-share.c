#include <stdio.h>

int main() {
    int n;
    int i = 0;
    while(i<=2){
        scanf("%d", &n);
        if(n%2==0){
            i++;
            printf("%d\n", n/2);
        }
    }
    return 0;
}