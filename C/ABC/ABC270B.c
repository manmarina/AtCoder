#include <stdio.h>

int main(void)
{
    int X, Y, Z;
    if (scanf("%d %d %d", &X, &Y, &Z) != 3)
        return 0;

    if (0 < X)
    {
        if (Y < 0 || X < Y)
        {
            printf("%d\n", X);
        }
        else if (Y < Z)
        {
            printf("-1\n");
        }
        else if (Z > 0)
        {
            printf("%d\n", X);
        }
        else
        {
            printf("%d\n", X - (Z * 2));
        }
    }
    else
    {
        if (Y > 0 || X > Y)
        {
            printf("%d\n", -X);
        }
        else if (Y > Z)
        {
            printf("-1\n");
        }
        else if (Z < 0)
        {
            printf("%d\n", -X);
        }
        else
        {
            printf("%d\n", -X + (Z * 2));
        }
    }

    return 0;
}
