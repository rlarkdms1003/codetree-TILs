#include <stdio.h>

int main() {
    int a_math, a_eng, b_math, b_eng;
    scanf("%d %d", &a_eng, &a_math);
    scanf("%d %d", &b_eng, &b_math);
    if (a_eng>b_eng && a_math > b_math) {
        printf("1");
    }
    else {
        printf("0");
    }
    return 0;
}