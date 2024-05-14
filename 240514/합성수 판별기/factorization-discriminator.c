#include <stdio.h>
#include <stdbool.h>
int main() {
    int n;
    bool satisfied = false;
    scanf("%d", &n);
    for(int i=2; i<=n; i++) {
        if(n%i==0) {
            satisfied = true;
        }
    }
    if(satisfied == true) {
        printf("C");
    }
    else {
        printf("N");
    }
    return 0;
}