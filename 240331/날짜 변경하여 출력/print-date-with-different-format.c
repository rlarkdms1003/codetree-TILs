#include <stdio.h>

int main() {
    int yyyy, mm, dd;
    scanf("%d.%d.%d", &yyyy, &mm, &dd);
    printf("%d-%d-%d", mm, dd, yyyy);
    return 0;
}