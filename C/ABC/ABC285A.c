#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d%d", &a, &b);

    if (b / 2 == a)
    {
        puts("Yes");
    }
    else
    {
        puts("No");
    }

    return 0;
}
