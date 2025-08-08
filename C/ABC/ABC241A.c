#include <stdio.h>

int main(void)
{
    int a[100]; // 入力される要素数に応じて十分大きく確保
    int n = 0;

    // スペース区切りの整数をすべて読み込む
    while (scanf("%d", &a[n]) == 1)
    {
        n++;
    }

    // a[a[a[0]]] を計算して出力
    printf("%d\n", a[a[a[0]]]);

    return 0;
}
