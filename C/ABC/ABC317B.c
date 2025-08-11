#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main(void)
{
    int N;
    scanf("%d", &N);

    int A[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    qsort(A, N, sizeof(int), cmp);

    for (int i = 0; i < N - 1; i++)
    {
        if (A[i + 1] - A[i] != 1)
        {
            printf("%d\n", A[i] + 1);
            return 0;
        }
    }

    return 0;
}
