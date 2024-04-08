#include <stdio.h>

int main() {
    int a_eng, a_math, b_eng, b_math;
    scanf("%d %d", &a_math, &a_eng);
    scanf("%d %d", &b_math, &b_eng);
    if (a_math > b_math && (a_eng <= b_eng || a_eng > b_eng)) {
        printf("A");
    }
    else {
        printf("B");
    }
    return 0;
}