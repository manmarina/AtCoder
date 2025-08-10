#include <stdio.h>

int main(void)
{
    double N;
    scanf("%lf", &N); // 実数入力

    printf("%d\n", (int)(N + 0.5)); // 普通の四捨五入
    return 0;
}
