#include <stdio.h>

int main() {
    int al;
    scanf("%c", &al);
    if (al=='S') {
        printf("Superior");
    }
    else if (al=='A') {
        printf("Excellemt");
    }
    else if (al=='B') {
        printf("Good");
    }
    else if (al=='C') {
        printf("Usually");
    }
    else if (al=='D') {
        printf("Effort");
    }
    else {
        printf("Failure");
    }
    return 0;
}