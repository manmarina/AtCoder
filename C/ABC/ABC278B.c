#include <stdio.h>

int main(void)
{
    int H, M;
    scanf("%d %d", &H, &M);

    if (5 < H && H < 10)
    {
        H = 10;
        M = 0;
    }
    else if (15 < H && H < 20)
    {
        H = 20;
        M = 0;
    }

    if (20 <= H && H <= 22 && M > 39)
    {
        H++;
        M = 0;
    }
    else if (H == 23 && M > 39)
    {
        H = 0;
        M = 0;
    }

    printf("%d %d\n", H, M);

    return 0;
}
