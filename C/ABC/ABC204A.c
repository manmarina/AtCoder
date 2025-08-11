#include <stdio.h>

int main(void)
{
    int x, y;
    scanf("%d %d", &x, &y);

    if (x == y)
    {
        printf("%d\n", x);
    }
    else
    {
        printf("%d\n", 3 - (x + y));
    }

    return 0;
}
