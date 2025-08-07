#include <stdio.h>

int main(void)
{
    int N;
    char S[1001]; // N の最大値に応じて十分な長さを確保

    scanf("%d", &N);
    scanf("%s", S);

    // 最後の文字を出力
    printf("%c\n", S[N - 1]);

    return 0;
}
