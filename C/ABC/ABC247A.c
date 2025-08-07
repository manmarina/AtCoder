#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char bin[10];
    scanf("%s", bin);

    // 2進数文字列を10進数のintに変換
    int S = (int)strtol(bin, NULL, 2);

    // 1ビット右シフト
    S = S >> 1;

    // 4桁の2進数で出力（先頭に0を埋める）
    for (int i = 3; i >= 0; i--)
    {
        putchar((S & (1 << i)) ? '1' : '0');
    }
    putchar('\n');

    return 0;
}
