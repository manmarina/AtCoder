#include <stdio.h>

int main(void)
{
    int N, A, X, Y;
    scanf("%d %d %d %d", &N, &A, &X, &Y);

    int total;
    if (N <= A)
    {
        total = N * X;
    }
    else
    {
        total = X * A;
        total += Y * (N - A);
    }

    printf("%d\n", total);
    return 0;
}
