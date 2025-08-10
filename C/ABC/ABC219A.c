#include <stdio.h>

int main(void)
{
    int X;
    scanf("%d", &X);

    if (X < 40)
    {
        printf("%d\n", 40 - X);
    }
    else if (X < 70)
    {
        printf("%d\n", 70 - X);
    }
    else if (X < 90)
    {
        printf("%d\n", 90 - X);
    }
    else
    {
        printf("expert\n");
    }

    return 0;
}
