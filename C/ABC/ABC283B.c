#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int *A = (int *)malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    int Q;
    scanf("%d", &Q);

    // 出力用バッファ（最大でもQ行）
    int *outs = (int *)malloc(sizeof(int) * Q);
    int outc = 0;

    for (int i = 0; i < Q; i++)
    {
        int t, x, y;
        scanf("%d", &t);
        if (t == 1)
        {
            scanf("%d %d", &x, &y);
            A[x - 1] = y; // 逐次更新
        }
        else
        {
            scanf("%d", &x);
            outs[outc++] = A[x - 1]; // 逐次計算 → 出力だけ貯める
        }
    }

    // まとめて出力
    for (int i = 0; i < outc; i++)
    {
        printf("%d\n", outs[i]);
    }

    free(outs);
    free(A);
    return 0;
}
