#include <stdio.h>

int main() {
    int number;
    scanf("%d", &number);
    if (number==1) {
        printf("John");
    }
    else if(number==2) {
        printf("Tom");
    }
    else if(number==3) {
        printf("Paul");
    }
    else {
        printf("vacancy");
    }
    return 0;
}