#include <stdio.h>

int main()
{
    char S[101];
    scanf("%s", S);

    int i = 0;
    int count = 0;
    while (S[i] != '\0')
    {
        if (S[i] == 'v')
            count++;
        else
            count += 2;
        i++;
    }

    printf("%d\n", count);

    return 0;
}
