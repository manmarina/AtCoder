#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);

    char S[N][11];
    for (int i = 0; i < N; i++)
        scanf("%s", S[i]);

    for (int i = 0; i < N; i++)
        printf("%s\n", S[N - 1 - i]);

    return 0;
}
