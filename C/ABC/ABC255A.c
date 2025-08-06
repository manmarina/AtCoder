#include <stdio.h>

int main()
{
    int R, C;
    scanf("%d%d", &R, &C);

    int A[2][2];
    scanf("%d%d", &A[0][0], &A[0][1]);
    scanf("%d%d", &A[1][0], &A[1][1]);

    printf("%d\n", A[R - 1][C - 1]);

    return 0;
}
