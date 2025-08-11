#include <stdio.h>

int main(void)
{
    int H, W;
    scanf("%d %d", &H, &W);

    int X[1000] = {0}; // Wの最大値に合わせて調整
    char C[1001];      // 1行分の入力用（終端文字分+1）

    for (int i = 0; i < H; i++)
    {
        scanf("%s", C); // 1行読み込み
        for (int j = 0; j < W; j++)
        {
            if (C[j] == '#')
            {
                X[j]++;
            }
        }
    }

    for (int j = 0; j < W; j++)
    {
        if (j > 0)
            printf(" ");
        printf("%d", X[j]);
    }
    printf("\n");

    return 0;
}
