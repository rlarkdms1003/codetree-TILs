#include <stdio.h>

int main() {
    int val;
    int sum_val=0;
    for(int i=0; i<10; i++) {
        scanf("%d", &val);
        sum_val += val;
    }
    printf("%d", sum_val);
    return 0;
}