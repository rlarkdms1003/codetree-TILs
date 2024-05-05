#include <stdio.h>

int main() {
    int n, i;
    int cls=0; int cor=0; int rest=0;
    scanf("%d", &n);
    for(i=1; i<=n; i++) {
        if(i%12==0) {
            rest++;
        }
        else if(i%3==0 && i%2==0 || i%3==0) {
            cor++;
        }
        else if(i%2==0) {
            cls++;
        }
    }
    printf("%d %d %d", cls, cor, rest);
    return 0;
}