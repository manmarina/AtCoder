#include <stdio.h>

int main(void)
{
    char S[4]; // 3文字＋終端
    scanf("%3s", S);

    int seen[26] = {0};
    int length = 0;

    for (int i = 0; i < 3; i++)
    {
        int idx = S[i] - 'a';
        if (!seen[idx])
        {
            seen[idx] = 1;
            length++;
        }
    }

    int count = 1;
    if (length == 3)
    {
        count = 6;
    }
    else if (length == 2)
    {
        count = 3;
    }

    printf("%d\n", count);
    return 0;
}
