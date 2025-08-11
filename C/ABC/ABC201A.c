#include <stdio.h>

int main(void)
{
    int A[3];
    // 入力
    scanf("%d %d %d", &A[0], &A[1], &A[2]);

    // 昇順にソート（バブルソート）
    for (int i = 0; i < 2; i++)
    {
        for (int j = i + 1; j < 3; j++)
        {
            if (A[i] > A[j])
            {
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
    }

    // 差が等しいか判定
    if (A[1] - A[0] == A[2] - A[1])
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
