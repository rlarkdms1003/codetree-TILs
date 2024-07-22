#include <stdio.h>

int main() {
    int n;
    int cnt=1;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        if(i%2==0) {
            for(int j=0; j<n; j++) {
                printf("%d", cnt);
                cnt++;
            }
        }
        else {
            for(int j=n; j>0; j--) {
                printf("%d", cnt-1);
                cnt--;
            }
        }
        printf("\n");
    }
    return 0;
}