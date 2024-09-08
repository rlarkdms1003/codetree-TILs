#include <stdio.h>

int main() {
    int arr[10];
    int sum =0;
    int mean=0;
    int cnt=0;
    for(int i=0; i<10;i++) {
        scanf("%d", &arr[i]);
        if(i%2==1) {
            sum +=arr[i];
        }
        if(i==2 || i==5|| i==8) {
            mean += arr[i];
            cnt++;
        }
    }
    printf("%d %.1f", sum, (double)mean/cnt);
    return 0;
}