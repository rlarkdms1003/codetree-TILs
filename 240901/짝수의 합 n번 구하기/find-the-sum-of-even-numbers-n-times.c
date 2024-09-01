#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        int a,b=0;
        int sum=0;
        scanf("%d %d", &a, &b);
        if (a%2!=0) {
            a++;
        }
        for(int j=a; j<=b; j+=2) {
                sum +=j;
            }
            
    printf("%d",sum);
    printf("\n");
    }
    return 0;
}