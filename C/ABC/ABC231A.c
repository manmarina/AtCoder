#include <stdio.h>

int main(void)
{
    int D;
    scanf("%d", &D);

    // 浮動小数点計算にするため100.0を使う
    printf("%f\n", D / 100.0);

    return 0;
}
