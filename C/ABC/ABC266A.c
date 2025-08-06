#include <stdio.h>
#include <string.h>

int main()
{
    char S[100];
    scanf("%s", S);

    int len = (int)strlen(S);
    printf("%c\n", S[len / 2]);

    return 0;
}
