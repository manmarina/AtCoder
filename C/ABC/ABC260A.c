#include <stdio.h>

int main()
{
    char S[4]; // 3文字 + 終端文字
    scanf("%s", S);

    for (int i = 0; i < 3; i++)
    {
        int count = 0;
        for (int j = 0; j < 3; j++)
        {
            if (S[i] == S[j])
            {
                count++;
            }
        }
        if (count == 1)
        {
            putchar(S[i]);
            putchar('\n');
            return 0;
        }
    }

    printf("-1\n");
    return 0;
}
