#include <stdio.h>

int main() {
    char arr[10];
    for(int i=0;i<10;i++) {
        scanf(" %c", &arr[i]);
        if(i==1 || i==4|| i==7) {
           printf("%c ", arr[i]);
        }
    }
    return 0;
}