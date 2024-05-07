#include <stdio.h>

int main() {
    int i;
    int sum=0;
    double avg=0;
    int cnt = 0;
    for(i=1; i<=10; i++) {
        int n;
        scanf("%d\n", &n);
        if(n>=0 && n<=200) {
            sum += n;
            cnt++;
        }
    }
    avg = (double)sum/cnt;
    printf("%d %.1lf", sum, avg); 
    return 0;
}