#include <stdio.h>

int main() {
    int a_age, b_age;
    char a_sex, b_sex;
    scanf("%d %c", &a_age, &a_sex);
    scanf("%d %c", &b_age, &b_sex);
    if(a_age && a_sex >=19 || b_age && b_sex >=19) {
        printf("1");
    }
    else if ((a_age && a_sex >= 19) && (b_age && b_sex >=19)){
        printf("1");
    }
    else {
        printf("0");
    }

    return 0;
}