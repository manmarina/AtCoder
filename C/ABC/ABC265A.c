#include <stdio.h>

int main()
{
    int X, Y, N;
    scanf("%d%d%d", &X, &Y, &N);

    int total = 0;
    if (Y > X * 3)
        total = X * N;
    else
    {
        int Y_count = N / 3;
        int Y_total = Y * Y_count;
        int X_count = N % 3;
        int X_total = X * X_count;
        total = Y_total + X_total;
    }

    printf("%d\n", total);

    return 0;
}
