#include <stdio.h>

int main()
{
    int N, H, X;
    scanf("%d%d%d", &N, &H, &X);

    int P[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &P[i]);

    int diff = X - H;
    for (int i = 0; i < N; i++)
    {
        if (P[i] >= diff)
        {
            printf("%d\n", i + 1);
            break;
        }
    }

    return 0;
}
