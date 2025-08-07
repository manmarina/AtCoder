#include <stdio.h>

int main()
{
    char S[4];
    scanf("%s", S);

    int i = 0;
    while (S[i] != '\0')
        i++;

    int times = 6 / i;
    for (int j = 0; j < times; j++)
        printf("%s", S);
    putchar('\n');

    return 0;
}