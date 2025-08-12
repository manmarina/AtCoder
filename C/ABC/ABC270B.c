#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int X, Y, Z;
    if (scanf("%d %d %d", &X, &Y, &Z) != 3)
        return 0;

    if ((0 < Y && Y < X && X < Z) ||
        (0 < Y && Y < Z && Z < X) ||
        (X < Z && Z < Y && Y < 0) ||
        (Z < X && X < Y && Y < 0))
    {
        printf("-1\n");
    }
    else if ((Z < 0 && 0 < Y && Y < X) ||
             (X < Y && Y < 0 && 0 < Z))
    {
        printf("%d\n", 2 * abs(Z) + abs(X));
    }
    else
    {
        printf("%d\n", abs(X));
    }

    return 0;
}
