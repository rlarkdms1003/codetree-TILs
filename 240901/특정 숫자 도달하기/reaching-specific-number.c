#include <stdio.h>

int main() {
    int arr[10];
    int sum=0;
    int cnt=0;
    for(int i=0; i<10; i++) {
        scanf("%d", &arr[i]);
        if(arr[i]<250) {
            sum +=arr[i];
            cnt++;
        }
        else {
            break;
        }
    }
    printf("%d %.1f", sum, ((double)sum/cnt));
    return 0;
}