#include <stdio.h>

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int N, P, Q, R, S;
    scanf("%d%d%d%d%d", &N, &P, &Q, &R, &S);

    int A[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    for (int i = 0; i < Q - P + 1; i++)
        swap(&A[P - 1 + i], &A[R - 1 + i]);

    for (int i = 0; i < N; i++)
        printf("%d ", A[i]);
    putchar('\n');

    return 0;
}
