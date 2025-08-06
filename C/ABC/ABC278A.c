#include <stdio.h>

int main()
{
    int N, K;
    scanf("%d%d", &N, &K);

    int A[N + K];
    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    for (int i = N; i < N + K; i++)
        A[i] = 0;

    for (int i = K; i < N + K; i++)
        printf("%d ", A[i]);
    putchar('\n');

    return 0;
}
