#include <stdio.h>

int main() {
    int a_temp, a_cold, b_temp, b_cold, c_temp, c_cold;
    scanf("%d %d", &a_cold, &a_temp);
    scanf("%d %d", &b_cold, &b_temp);
    scanf("%d %d", &c_cold, &c_temp);

    if((a_cold=='Y' && a_temp>=37) && (b_cold=='Y' && b_temp>=37) &&(c_cold=='Y' && c_temp>=37)) {
        printf("A");
    }
    else if((a_cold=='Y' && a_temp>=37) && (b_cold=='Y' && b_temp>=37 || c_cold=='Y' && c_temp>=37)) {
        printf("A");
    }
    else if((b_cold=='Y' && b_temp>=37) && (c_cold=='Y' && c_temp=='Y')) {
        printf("A");
        }
        if('A'>=2) {
            printf("E");
        }
        else printf("N");

    return 0;
}