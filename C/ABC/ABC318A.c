#include <stdio.h>

int main()
{
    int N, M, P;
    scanf("%d%d%d", &N, &M, &P);

    int count = (N - M) / P + 1;
    printf("%d\n", count);

    return 0;
}
