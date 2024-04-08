#include <stdio.h>

int main() {
    int age, sex;
    scanf("%d", &sex);
    scanf("%d", &age);
    if (sex==0 && age>=19) {
        printf("MAN");
    }
    else if (sex==1 && age >=19) {
        printf("WOMAN");
    }
    else if (sex==0 && age <19) {
        printf("BOY");
    }
    else {
        printf("GIRL");
    }


    return 0;
}