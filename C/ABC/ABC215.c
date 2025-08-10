#include <stdio.h>
#include <string.h>

int main(void)
{
    char S[16];
    scanf("%s", S);

    if (strcmp(S, "Hello,World!") == 0)
    {
        printf("AC\n");
    }
    else
    {
        printf("WA\n");
    }

    return 0;
}
