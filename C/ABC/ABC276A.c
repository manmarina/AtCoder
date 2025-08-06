#include <stdio.h>

int main()
{
    char S[101];
    scanf("%s", S);

    int index = -1;
    int i = 0;
    while (S[i] != '\0')
    {
        if (S[i] == 'a')
            index = i + 1;
        i++;
    }
    printf("%d\n", index);

    return 0;
}
