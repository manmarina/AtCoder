#include <stdio.h>
#include <string.h>

int main(void)
{
    char S[101]; // 最大100文字+終端
    int a, b;

    scanf("%s", S); // 文字列読み込み
    scanf("%d %d", &a, &b);

    // インデックスは1始まりなので-1する
    char tmp = S[a - 1];
    S[a - 1] = S[b - 1];
    S[b - 1] = tmp;

    printf("%s\n", S);

    return 0;
}
