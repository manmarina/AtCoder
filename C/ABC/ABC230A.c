#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    if (N >= 42)
    {
        N += 1;
    }

    // 3桁ゼロ埋めで表示
    printf("AGC%03d\n", N);

    return 0;
}
