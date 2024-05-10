#include <stdio.h>

int main() {
    int a, b;
    int i;
    char d;
    while(1) {
        scanf("%d %d %c", &a, &b, &d);
        printf("%d\n", a*b);
        if(d=='C') {
            break;
        }
    }
    return 0;
}