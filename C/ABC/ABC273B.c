#include <stdio.h>

int main(void)
{
    unsigned long long X;
    int K;
    if (scanf("%llu %d", &X, &K) != 2)
        return 0;

    unsigned long long base = 10; // 10^(0+1)
    for (int i = 0; i < K; i++)
    {
        // 整数だけで四捨五入（0.5を足してから割る）
        X = ((X + base / 2) / base) * base;

        // 次の桁へ（10倍）: 最大でも 10^15 まで
        base *= 10;
    }

    printf("%llu\n", X);
    return 0;
}
