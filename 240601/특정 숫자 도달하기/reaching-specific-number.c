#include <stdio.h>

int main() {
    int val;
    int sum_val=0;
    int cnt=0;
    double avg=0;
    for(int i=0; i<10; i++) {
        scanf("%d", &val);
        if(val<250) {
            cnt++;
            sum_val += val;
        }
        else {
            break;
        }
        avg= (double)sum_val/cnt;
    }
    printf("%d %.1f", sum_val, avg);
    return 0;
}