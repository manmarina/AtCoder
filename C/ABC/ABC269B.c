#include <stdio.h>
#include <string.h>

int main(void)
{
    char S[10][11]; // 10文字 + 終端
    for (int i = 0; i < 10; i++)
    {
        scanf("%10s", S[i]);
    }

    int D = 10;
    int flag = 0;
    int A = 0, B = 0, colC = 0; // colC は Python の C に対応
    // 最初の '#' の位置を探す
    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (S[i][j] == '#' && !flag)
            {
                A = i + 1; // 1-based
                colC = j + 1;
                flag = 1;
            }
            if (S[i][j] == '.' && flag)
            {
                D = j;
                break;
            }
        }
        if (flag)
            break;
    }

    B = 10;
    flag = 0;
    // A 行目以降で '#' が無くなった行を探す
    for (int i = A - 1; i < 10; i++)
    {
        int hasSharp = 0;
        for (int j = 0; j < 10; j++)
        {
            if (S[i][j] == '#')
            {
                hasSharp = 1;
                break;
            }
        }
        if (!hasSharp)
        {
            B = i; // 1-based
            flag = 1;
            break;
        }
    }

    printf("%d %d\n", A, B);
    printf("%d %d\n", colC, D);

    return 0;
}
