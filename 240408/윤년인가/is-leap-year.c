#include <stdio.h>

int main() {
    int y;
    scanf("%d", &y);
    if (y/4!=0) {
        if (y/100==0 && y/400!=0) {
            printf("false");
        }
        else {
            printf("true");
        }
    }
    return 0;
}