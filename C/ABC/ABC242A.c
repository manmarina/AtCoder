#include <stdio.h>

int main(void)
{
    double A, B, C, X;
    scanf("%d%d%d%d", &A, &B, &C, &X);

    if (X <= A)
        puts("1");
    else if (X > B)
        puts("0");
    else
        printf("%.12f\n", C / (B - A));

    return 0;
}