#include <stdio.h>

int main()
{
    int A, B;
    scanf("%d", &A);

    for (int i = 65; i < 65 + A; i++)
        printf("%c", i);

    putchar('\n');

    return 0;
}
