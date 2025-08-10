#include <stdio.h>

int main(void)
{
    int N, K, A;
    scanf("%d %d %d", &N, &K, &A);

    // box1 の初期化 (A から N)
    int box1[2000]; // 十分なサイズを確保（N最大値次第で調整）
    int len = 0;
    for (int i = A; i <= N; i++)
    {
        box1[len++] = i;
    }

    // box2 = 1 から N
    int box2[1000]; // Nの最大値に合わせて確保
    for (int i = 1; i <= N; i++)
    {
        box2[i - 1] = i;
    }

    // 1000 // N + 1 回繰り返し
    for (int i = 0; i < 1000 / N + 1; i++)
    {
        for (int j = 0; j < N; j++)
        {
            box1[len++] = box2[j];
        }
    }

    // K番目(1-index)を出力
    printf("%d\n", box1[K - 1]);

    return 0;
}
