#include <stdio.h>

int main() {
    double arr[8];
    int n=0;
    double avg=0;
    double sum_val=0;
    for(int i=0; i<8; i++) {
        scanf("%lf", &arr[i]);
        n++;
        sum_val+= arr[i];
        avg = sum_val/n;
    }
    printf("%.1f", avg);
    return 0;
}