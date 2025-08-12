#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N, M;
    long long T;
    if (scanf("%d %d %lld", &N, &M, &T) != 3)
        return 0;

    // A[1..N-1] を使うので N 要素ぶん確保して先頭を 0 にしておく
    long long *A = (long long *)calloc(N, sizeof(long long));
    long long *bonus = (long long *)calloc(N + 1, sizeof(long long)); // bonus[1..N]
    if (!A || !bonus)
        return 0;

    for (int i = 1; i <= N - 1; i++)
        scanf("%lld", &A[i]);

    for (int i = 0; i < M; i++)
    {
        int X;
        long long Y;
        scanf("%d %lld", &X, &Y);
        bonus[X] = Y;
    }

    for (int i = 1; i <= N - 1; i++)
    {
        T += bonus[i];
        T -= A[i];
        if (T <= 0)
        {
            puts("No");
            free(A);
            free(bonus);
            return 0;
        }
    }

    puts("Yes");
    free(A);
    free(bonus);
    return 0;
}
