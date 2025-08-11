#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int price = (int)(N * 1.08);
    int regular_price = 206;

    if (price == regular_price)
    {
        printf("so-so\n");
    }
    else if (price < regular_price)
    {
        printf("Yay!\n");
    }
    else
    {
        printf(":(\n");
    }

    return 0;
}
