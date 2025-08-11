#include <stdio.h>

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    if (A == 0)
    {
        printf("Silver\n");
    }
    else if (B == 0)
    {
        printf("Gold\n");
    }
    else
    {
        printf("Alloy\n");
    }

    return 0;
}
