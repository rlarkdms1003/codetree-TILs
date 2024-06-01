#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    double arr[5];
    int cnt=0;
    double sum_val=0;
    double avg=0;
    for(int i=0; i<n; i++) {
        scanf("%lf", &arr[i]);
        sum_val += arr[i];
        avg =sum_val/n;
    }
    printf("%.1f", avg);
    if(avg>=4.0) {
        printf("\nPerfect");
    }
    else if(avg>=3.0) {
        printf("\nGood");
    }
    else {
        printf("\nPoor");
    }
    return 0;
}