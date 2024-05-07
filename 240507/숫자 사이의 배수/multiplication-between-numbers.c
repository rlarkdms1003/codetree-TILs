#include <stdio.h>

int main() {
    int a, b, i;
    int sum=0;
    int cnt=0;
    scanf("%d %d", &a, &b);
    for(i=a; i<=b; i++) {
        if(i%5==0 || i%7==0) {
            sum+= i;
            cnt++;

        }
    }
    double average= (double)sum/cnt;
    printf("%d %.1lf", sum, average);
    return 0;
}