#include <stdio.h>

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    if (A > B)
    {
        printf("0\n");
    }
    else
    {
        printf("%d\n", B - A + 1);
    }

    return 0;
}
