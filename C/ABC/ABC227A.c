#include <stdio.h>

int main(void)
{
    int N, K, A;
    scanf("%d %d %d", &N, &K, &A);

    int ans = (A + K - 1) % N;

    if (ans == 0)
    {
        printf("%d\n", N);
    }
    else
    {
        printf("%d\n", ans);
    }

    return 0;
}
