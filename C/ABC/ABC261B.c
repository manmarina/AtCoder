#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    if (scanf("%d", &N) != 1)
        return 0;

    // 行列Aを文字列として読み込む（各行は長さN）
    char **A = (char **)malloc(N * sizeof(char *));
    if (!A)
        return 0;
    for (int i = 0; i < N; i++)
    {
        A[i] = (char *)malloc((N + 1) * sizeof(char)); // 末尾の'\0'分+1
        if (!A[i])
            return 0;
        scanf("%s", A[i]);
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (i == j)
                continue;
            char ij = A[i][j];
            char ji = A[j][i];
            if ((ij == 'W' && ji != 'L') ||
                (ij == 'L' && ji != 'W') ||
                (ij == 'D' && ji != 'D'))
            {
                puts("incorrect");
                return 0;
            }
        }
    }

    puts("correct");
    return 0;
}
