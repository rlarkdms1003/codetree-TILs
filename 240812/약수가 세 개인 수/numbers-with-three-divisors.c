#include <stdio.h>

int main() {
    int s, e;
    int sum =0;
    scanf("%d %d", &s, &e);
    for(int i=s; i<=e; i++) {
        int cnt=0;
        for(int j=1; j<=i; j++) {
            if(i%j==0) {
                cnt++;
            }
        }
        if(cnt==3) {
            sum++;
        }
    }
    printf("%d", sum);
    return 0;
}