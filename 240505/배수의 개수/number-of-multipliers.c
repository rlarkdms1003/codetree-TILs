#include <stdio.h>

int main() {
    int n, i;
    int cnt=0;
    int cntt=0;
    for(i=0; i<10; i++) {
        scanf("%d\n", &n);
        if(n%3==0) {
            cnt++;
        }
        if(n%5==0) {
            cntt++;
        }
    }
    printf("%d %d", cnt, cntt);
    return 0;
}