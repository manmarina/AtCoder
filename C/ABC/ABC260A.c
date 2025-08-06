#include <stdio.h>

int main()
{
    char S[4];
    scanf("%s", S);

    if (S[0] == S[1] && S[1] == S[2])
        puts("-1");
    else if (S[0] == S[1] && S[1] != S[2])
        printf("%c\n", S[2]);
    else if (S[0] != S[1] && S[1] == S[2])
        printf("%c\n", S[0]);
    else if (S[0] == S[2] && S[2] != S[1])
        printf("%c\n", S[1]);
    else
        printf("%c\n", S[0]);

    return 0;
}
