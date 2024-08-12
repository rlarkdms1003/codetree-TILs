#include <stdio.h>

int main() {

    int cnt=0;
    int start, end=0;
    scanf("%d %d", &start, &end);
    
        for(int j=start; j<=end; j++) {
            int sum = 0;
            for(int i=1; i<=j-1; i++) {
                if(j%i==0) {
                    sum += i;
                }
            }
            if(sum == j) {
                cnt++;
            }
        }
    printf("%d", cnt);
    return 0;
}