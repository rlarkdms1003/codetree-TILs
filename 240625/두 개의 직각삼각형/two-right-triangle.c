#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    // 1 ≤ n ≤ 10의 범위를 확인합니다.
    if (n < 1 || n > 10) {
        printf("Please enter a value between 1 and 10.\n");
        return 1; // 프로그램을 종료합니다.
    }

    // n번 반복하면서 각 줄을 출력합니다.
    for (int i = 0; i < n; i++) {
        // 첫 번째 별 부분을 출력합니다.
        for (int j = 0; j < n - i; j++) {
            printf("*");
        }
        // 중간 공백 부분을 출력합니다.
        for (int j = 0; j < 2 * i; j++) {
            printf(" ");
        }
        // 두 번째 별 부분을 출력합니다.
        for (int j = 0; j < n - i; j++) {
            printf("*");
        }
        // 줄바꿈을 합니다.
        printf("\n");
    }

    return 0;
}