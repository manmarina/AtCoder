#include <stdio.h>
#include <stdlib.h>

static int cmp_int(const void *a, const void *b)
{
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int main(void)
{
    int N, M;
    scanf("%d %d", &N, &M);

    // 1回目: 辺を読みつつ次数を数える（あとで再利用するので保存もする）
    int *A = (int *)malloc(sizeof(int) * M);
    int *B = (int *)malloc(sizeof(int) * M);
    int *deg = (int *)calloc(N, sizeof(int));
    if (!A || !B || !deg)
        return 0;

    for (int i = 0; i < M; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        --a;
        --b; // 0-based
        A[i] = a;
        B[i] = b;
        deg[a]++;
        deg[b]++; // 無向なので両方カウント
    }

    // オフセット作成（prefix sum）
    int *offset = (int *)malloc(sizeof(int) * (N + 1));
    if (!offset)
        return 0;
    offset[0] = 0;
    for (int i = 0; i < N; i++)
        offset[i + 1] = offset[i] + deg[i];

    // 隣接リスト本体（フラット配列 2M 要素）
    int *adj = (int *)malloc(sizeof(int) * (size_t)(offset[N]));
    if (!adj)
        return 0;

    // 現在書き込み位置カーソル
    int *cur = (int *)malloc(sizeof(int) * N);
    if (!cur)
        return 0;
    for (int i = 0; i < N; i++)
        cur[i] = offset[i];

    // 2回目: フラット配列に詰める（出力は1-basedなので +1 して格納）
    for (int i = 0; i < M; i++)
    {
        int a = A[i], b = B[i];
        adj[cur[a]++] = b + 1;
        adj[cur[b]++] = a + 1;
    }

    // 各頂点の隣接先をソートして出力
    for (int v = 0; v < N; v++)
    {
        int start = offset[v];
        int len = deg[v];
        qsort(adj + start, (size_t)len, sizeof(int), cmp_int);

        printf("%d", len);
        for (int k = 0; k < len; k++)
        {
            printf(" %d", adj[start + k]);
        }
        putchar('\n');
    }

    free(A);
    free(B);
    free(deg);
    free(offset);
    free(adj);
    free(cur);
    return 0;
}
