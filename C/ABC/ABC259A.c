#include <stdio.h>

int main()
{
    int N, M, X, T, D;
    scanf("%d%d%d%d%d", &N, &M, &X, &T, &D);

    int tall;
    if (X <= M)
        tall = T;
    else
        tall = T - D * (X - M);

    printf("%d\n", tall);

    return 0;
}
