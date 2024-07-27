#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    if(b > a) {
        if(b%2==0 && a%2==0) {
            for(int j=1; j<10; j++) {
                for(int i=b; i>=a; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>a) {
                printf(" / ");
            }
        }
        printf("\n");
    }
    }
    if(b%2==0 && a%2==1) {
            for(int j=1; j<10; j++) {
                for(int i=b; i>=a; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>a+1) {
                printf(" / ");
            }
        }
        printf("\n");
    }
    }
    if(b%2==1 && a%2==0) {
            for(int j=1; j<10; j++) {
                for(int i=b-1; i>=a; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>a) {
                printf(" / ");
            }
        }
        printf("\n");
    }
    }
    if(b%2==1 && a%2==1) {
            for(int j=1; j<10; j++) {
                for(int i=b-1; i>=a; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>a+1) {
                printf(" / ");
            }
        }
        printf("\n");
    }
    }            
    else if(a!=b && b%2==1) {
            for(int j=1; j<10; j++) {
                for(int i=a-1; i>b; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>2) {
                    printf(" / ");}
            }
            printf("\n");
        }
    }
    if(a==b && b%2==0) {
            for(int i=1; i<10; i++) {
            printf("%d * %d = %d", b, i, b*i);
            printf("\n");
            }
        }
    }
else {if(a%2==0 && b%2==0) {
            for(int j=1; j<10; j++) {
                for(int i=a; i>=b; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>b) {
                printf(" / ");
            }
        }
        printf("\n");
    }
    }
    else if(a%2==0 && b%2==1) {
        for(int j=1; j<10; j++) {
            for(int i=a; i<b; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>b) {
                    printf("/ ");
                }
            }
        }
    }
     else if(a%2==1 && b%2==0) {
        for(int j=1; j<10; j++) {
            for(int i=a-1; i>=b; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>b) {
                    printf(" / ");
                }
            }
            printf("\n");
        }
    }
     else if(a%2==1 && b%2==1) {
        for(int j=1; j<10; j++) {
            for(int i=a-1; i>b; i-=2) {
                printf("%d * %d = %d", i, j, i*j);
                if(i>b+1) {
                    printf(" / ");
                }
            }
            printf("\n");
        }
    }         
   
    }

    return 0;
}