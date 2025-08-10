#include <stdio.h>
#include <string.h>

int main(void)
{
    char S1[3], S2[3]; // 2文字＋終端 '\0'

    scanf("%s", S1);
    scanf("%s", S2);

    if (strcmp(S1, "#.") == 0 && strcmp(S2, ".#") == 0)
    {
        printf("No\n");
    }
    else if (strcmp(S1, ".#") == 0 && strcmp(S2, "#.") == 0)
    {
        printf("No\n");
    }
    else
    {
        printf("Yes\n");
    }

    return 0;
}
