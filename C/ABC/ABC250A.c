#include <stdio.h>

int main()
{
    int H, W;
    int R, C;
    scanf("%d %d", &H, &W);
    scanf("%d %d", &R, &C);

    int ans = 0;
    if (R > 1) // 上
        ans++;
    if (C > 1) // 左
        ans++;
    if (R < H) // 下
        ans++;
    if (C < W) // 右
        ans++;

    printf("%d\n", ans);
    return 0;
}
