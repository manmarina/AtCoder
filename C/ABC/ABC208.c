#include <stdio.h>

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    if (A > B)
    {
        printf("No\n");
    }
    else if (A * 6 >= B)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
