#include <stdio.h>

int main() {
    int n;
    int sum=0;
    int cnt=0;
    double avg;
    scanf("%d", &n);
    for(int i=1; i<=n; i++) {
        int a;
        scanf("%d\n", &a);
        if(a>=1 && a<=1000) {
            sum += a;
            cnt++;
        }
    }
    avg = (double)sum/cnt;
    printf("%d %.1lf", sum, avg);
    return 0;
}