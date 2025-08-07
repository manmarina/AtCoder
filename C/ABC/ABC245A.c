#include <stdio.h>

int main(void)
{
    int A, B, C, D;
    scanf("%d %d %d %d", &A, &B, &C, &D);

    // 分単位に変換して比較
    int takahashi = A * 60 + B;
    int aoki = C * 60 + D;

    if (takahashi <= aoki)
        printf("Takahashi\n");
    else
        printf("Aoki\n");

    return 0;
}
