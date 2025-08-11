#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int S[10]; // 必要に応じて配列サイズを調整
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &S[i]);
    }

    printf("%d", S[0]); // 最初の要素はそのまま出力
    for (int i = 1; i < N; i++)
    {
        printf(" %d", S[i] - S[i - 1]); // 差分を出力（スペース区切り）
    }
    printf("\n");

    return 0;
}