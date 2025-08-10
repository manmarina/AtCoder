#include <stdio.h>
#include <string.h>

int main(void)
{
    char S[21];
    scanf("%s", S);

    const char *suffix = "ist";
    int len = strlen(S);

    if (strcmp(&S[len - 2], "er") == 0)
    {
        suffix = "er";
    }

    printf("%s\n", suffix);

    return 0;
}
