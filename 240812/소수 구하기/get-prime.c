#include <stdio.h>
#include <stdbool.h>
int main() {
    int n;
    scanf("%d", &n);
    for(int i=2; i<=n; i++) {
        bool isprime = true;
        
        for(int j=2; j<i; j++) {
            if(i%j==0) isprime = false;
        }
        if(isprime)
        printf("%d ", i);
    }
    return 0;
}