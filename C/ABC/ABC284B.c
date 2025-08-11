#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    int N[100];      // 各テストケースの要素数
    int A[100][100]; // 最大100要素を仮定（必要に応じて調整）

    for (int i = 0; i < T; i++)
    {
        scanf("%d", &N[i]);
        for (int j = 0; j < N[i]; j++)
        {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < T; i++)
    {
        int count = 0;
        for (int j = 0; j < N[i]; j++)
        {
            if (A[i][j] % 2 != 0)
            {
                count++;
            }
        }
        printf("%d\n", count);
    }

    return 0;
}
