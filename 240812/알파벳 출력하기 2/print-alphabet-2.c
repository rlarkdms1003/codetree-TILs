#include <stdio.h>

int main() {
    int n;
    int cnt = 0;
    scanf("%d", &n);
    for(int i=n; i>0; i--) {
        for(int j=n; j>i; j--) {
            printf("  ");
        }
        for(int j =0; j<i; j++) {
            printf("%c ", 65+cnt);
            cnt++;
            if (65+cnt > 'Z') {
                cnt = 0;
            }
        }
        printf("\n");
    }
    return 0;
}