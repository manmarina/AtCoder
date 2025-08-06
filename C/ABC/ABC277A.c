#include <stdio.h>

int main()
{
    int N, X;
    scanf("%d%d", &N, &X);

    int P[N];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &P[i]);
    }

    for (int i = 0; i < N; i++)
    {
        if (P[i] == X)
        {
            printf("%d\n", i + 1);
            break;
        }
    }
    return 0;
}
