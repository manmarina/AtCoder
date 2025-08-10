#include <stdio.h>

int main(void)
{
    char S[4];
    scanf("%s", S); // 文字列として入力を受け取る

    // '0' の文字コードを引いて整数値に変換
    int result = (S[0] - '0') * (S[2] - '0');

    printf("%d\n", result);

    return 0;
}
