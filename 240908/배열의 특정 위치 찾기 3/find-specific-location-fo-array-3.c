#include <stdio.h>

int main() {
    int arr[100];
    int k=0;
    for(int i=0; i<100; i++) {
        scanf("%d", &arr[i]);
        if(arr[i]==0) {
            break;
        }
        k++;
    }
    if(k<3) {
        printf("-1");
    }
    else {
        printf("%d", arr[k-1]+arr[k-2]+arr[k-3]);}
    
    return 0;
}