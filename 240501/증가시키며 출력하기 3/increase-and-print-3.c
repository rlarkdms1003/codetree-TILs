#include <stdio.h>

int main() {
    int i=10;
    while(i%2==0 && i<=26) {
        printf("%d ", i);
        i+=2;
    }
    return 0;
}