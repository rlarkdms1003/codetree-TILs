#include <stdio.h>
#include <stdbool.h>
int main() {
    int n;
    int cnt=0;
    bool satisfied;
    for(int i=0; i<5; i++) {
        scanf("%d\n", &n);
        if(i%3==0) {
            satisfied == false;
            cnt++;
        }
    }
    if(cnt==5) {
        satisfied = false;
    }
    if(satisfied == false) {
        printf("1");
    }
    else {
        printf("0");
    }
     return 0;
}