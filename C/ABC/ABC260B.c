#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int score; // 点数
    int id;    // 受験番号(1-based)
} Entry;

// 得点降順、同点はid昇順
static int cmp_desc_score_asc_id(const void *a, const void *b)
{
    const Entry *x = (const Entry *)a;
    const Entry *y = (const Entry *)b;
    if (x->score != y->score)
        return (y->score - x->score);
    return (x->id - y->id);
}

// id昇順
static int cmp_id_asc(const void *a, const void *b)
{
    const int *x = (const int *)a;
    const int *y = (const int *)b;
    return (*x - *y);
}

int main(void)
{
    int N, X, Y, Z;
    if (scanf("%d %d %d %d", &N, &X, &Y, &Z) != 4)
        return 0;

    int *A = (int *)malloc(sizeof(int) * N);
    int *B = (int *)malloc(sizeof(int) * N);
    if (!A || !B)
        return 0;

    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);
    for (int i = 0; i < N; i++)
        scanf("%d", &B[i]);

    Entry *math = (Entry *)malloc(sizeof(Entry) * N);
    Entry *eng = (Entry *)malloc(sizeof(Entry) * N);
    Entry *both = (Entry *)malloc(sizeof(Entry) * N);
    if (!math || !eng || !both)
        return 0;

    for (int i = 0; i < N; i++)
    {
        int id = i + 1;
        math[i].score = A[i];
        math[i].id = id;
        eng[i].score = B[i];
        eng[i].id = id;
        both[i].score = A[i] + B[i];
        both[i].id = id;
    }

    qsort(math, N, sizeof(Entry), cmp_desc_score_asc_id);
    qsort(eng, N, sizeof(Entry), cmp_desc_score_asc_id);
    qsort(both, N, sizeof(Entry), cmp_desc_score_asc_id);

    // 選抜済みフラグ（1-basedで使う）
    char *picked = (char *)calloc(N + 1, sizeof(char));
    // 最終合格者のIDを格納
    int *ans = (int *)malloc(sizeof(int) * (X + Y + Z));
    int an = 0;

    // 数学からX人
    for (int i = 0, cnt = 0; i < N && cnt < X; i++)
    {
        int id = math[i].id;
        if (!picked[id])
        {
            picked[id] = 1;
            ans[an++] = id;
            cnt++;
        }
    }
    // 英語からY人
    for (int i = 0, cnt = 0; i < N && cnt < Y; i++)
    {
        int id = eng[i].id;
        if (!picked[id])
        {
            picked[id] = 1;
            ans[an++] = id;
            cnt++;
        }
    }
    // 合計からZ人
    for (int i = 0, cnt = 0; i < N && cnt < Z; i++)
    {
        int id = both[i].id;
        if (!picked[id])
        {
            picked[id] = 1;
            ans[an++] = id;
            cnt++;
        }
    }

    // 受験番号の昇順で出力
    qsort(ans, an, sizeof(int), cmp_id_asc);
    for (int i = 0; i < an; i++)
    {
        printf("%d\n", ans[i]);
    }

    free(A);
    free(B);
    free(math);
    free(eng);
    free(both);
    free(picked);
    free(ans);
    return 0;
}
