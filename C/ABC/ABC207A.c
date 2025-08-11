#include <stdio.h>

int main(void)
{
    int ABC[3];
    int i, j, temp;

    // 入力
    for (i = 0; i < 3; i++)
    {
        scanf("%d", &ABC[i]);
    }

    // 昇順ソート（単純交換ソート）
    for (i = 0; i < 3; i++)
    {
        for (j = i + 1; j < 3; j++)
        {
            if (ABC[i] > ABC[j])
            {
                temp = ABC[i];
                ABC[i] = ABC[j];
                ABC[j] = temp;
            }
        }
    }

    // 2番目と3番目の要素の和を出力
    printf("%d\n", ABC[1] + ABC[2]);

    return 0;
}
