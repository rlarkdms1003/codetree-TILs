#include <stdio.h>

int main() {
    double a, b;
    scanf("%lf", &a);
    scanf("%lf", &b);
    if (a>=1.0 && b>=1.0) {
        printf("High");
    }
    else if (a>=0.5 && b>=0.5) {
        printf("Middle");
    }
    else {
        printf("Low");
    }
    return 0;
}