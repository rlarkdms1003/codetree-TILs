#include <stdio.h>
#include <stdbool.h>
int main() {
    int n;
    bool satisfied = false;
    scanf("%d", &n);
    for(int i=1; i<n; i++) {
        if(n%i!=0) {
            satisfied = true;
        }
    }
    if(satisfied == true) {
        printf("P");
    }
    else {
        printf("C");
    }

    return 0;
}