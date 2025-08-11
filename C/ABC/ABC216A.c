#include <stdio.h>

int main(void)
{
    double XY;
    scanf("%lf", &XY);

    int Y = (int)((XY - (int)XY) * 10);
    char sign;

    if (Y < 3)
    {
        sign = '-';
    }
    else if (Y < 7)
    {
        sign = '\0'; // 空文字列の代わりに終端文字
    }
    else
    {
        sign = '+';
    }

    if (sign == '\0')
    {
        printf("%d\n", (int)XY);
    }
    else
    {
        printf("%d%c\n", (int)XY, sign);
    }

    return 0;
}
