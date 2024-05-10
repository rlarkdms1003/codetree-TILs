#include <stdio.h>

int main() {
    int n;    
    int sum=0;
    int cnt=0;
    double avg=0;
    while(1) {
        scanf("%d\n", &n);
        if(n>=20 && n<30) {
            sum += n;
            cnt++;
            }
        else {
            break;
        }

    }
    avg = (double)sum/cnt;
    printf("%.2lf", avg);
    
    return 0;
}