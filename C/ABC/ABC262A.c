#include <stdio.h>

int main()
{
    int Y;
    scanf("%d", &Y);

    while (1)
    {
        if (Y % 4 == 2)
        {
            printf("%d\n", Y);
            break;
        }
        Y++;
    }

    return 0;
}
