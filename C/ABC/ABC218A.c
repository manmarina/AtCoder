#include <stdio.h>

int main(void)
{
    int N;
    char S[8];

    scanf("%d", &N);
    scanf("%s", S);

    if (S[N - 1] == 'o')
        printf("Yes\n");
    else
        printf("No\n");

    return 0;
}
