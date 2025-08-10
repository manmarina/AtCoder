#include <stdio.h>
#include <string.h> // strcmp() に必要

int main(void)
{
    char S[11], T[11];
    scanf("%s %s", S, T);

    if (strcmp(S, T) < 0) // S < T の場合
        printf("Yes\n");
    else
        printf("No\n");

    return 0;
}
