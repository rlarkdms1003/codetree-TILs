#include <stdio.h>

int main() {
    int i=0;
    int arr[10];
    for(int i=0; i<10; i++) {
        scanf("%c ", &arr[i]);
    }
    for(int i=9; i>=0; i--) {
        printf("%c", arr[i]);
    }
    return 0;
}