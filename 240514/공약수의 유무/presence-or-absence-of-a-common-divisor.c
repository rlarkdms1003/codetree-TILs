#include <stdio.h>
#include <stdbool.h>
int main() {
    int a,b;
    bool satisfied = false;
    scanf("%d %d", &a, &b);
    for(int i=1; i<=b; i++) {
        if(a%i==0 && b%i==0) {
            satisfied = true;
        }
        
    }
    if(satisfied== true) {
        printf("1");
    }
    else {
        printf("0");
    }

    return 0;
}