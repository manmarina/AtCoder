#include <stdio.h>
#include <stdlib.h> // abs() 関数に必要

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);

    if (abs(a - b) == 1 || abs(a - b) == 9)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
