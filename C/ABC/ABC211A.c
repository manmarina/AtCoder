#include <stdio.h>

int main(void)
{
    int A, B;
    double C;

    scanf("%d %d", &A, &B);

    C = (A - B) / 3.0 + B; // 3.0 として浮動小数点除算に
    printf("%f\n", C);

    return 0;
}
