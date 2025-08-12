#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N, Q;
    scanf("%d %d", &N, &Q);

    // a[i] の列数は可変なのでポインタ配列で確保
    int **a = malloc(N * sizeof(int *));
    if (!a)
        return 1;

    for (int i = 0; i < N; i++)
    {
        int L;
        scanf("%d", &L); // 各行の最初に列数が来る想定（Pythonのlist(map())に対応）
        a[i] = malloc(L * sizeof(int));
        if (!a[i])
            return 1;
        for (int j = 0; j < L; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    int *answer = malloc(Q * sizeof(int));
    if (!answer)
        return 1;

    for (int i = 0; i < Q; i++)
    {
        int s, t;
        scanf("%d %d", &s, &t);
        answer[i] = a[s - 1][t - 1];
    }

    for (int i = 0; i < Q; i++)
    {
        printf("%d\n", answer[i]);
    }

    // メモリ解放
    for (int i = 0; i < N; i++)
    {
        free(a[i]);
    }
    free(a);
    free(answer);

    return 0;
}
