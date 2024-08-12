#include <stdio.h>

int main() {
    int n;
    int cnt =0;
    scanf("%d", &n);
    for(int i=1;i<=n; i++) {
        for(int j=1; j<=i; j++) {
            printf("%c", 65+cnt);
            cnt++;
            if(65+cnt > 'Z') {
                cnt = 0;
            }
        }
        printf("\n");
    }
    return 0;
}