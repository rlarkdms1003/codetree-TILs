#include <stdio.h>

int main() {
    int n, i;
    int cnt=0;
    int year=0;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        if(i%4==0) {
            cnt++;
            if(i%100==0 && i%400!=0) {
                year++;
            }
        }
    }
    printf("%d", cnt-year);
    return 0;
}