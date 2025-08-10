#include <stdio.h>

int main(void)
{
    int X, Y;
    scanf("%d%d", &X, &Y);

    int count = 0;
    if (X < Y)
    {
        int diff = Y - X;
        count = diff / 10;
        if (diff % 10 > 0)
            count++;
    }

    printf("%d\n", count);
    return 0;
}
