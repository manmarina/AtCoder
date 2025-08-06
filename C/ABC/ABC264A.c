#include <stdio.h>

int main()
{
    int L, R;
    scanf("%d%d", &L, &R);

    char *str = "atcoder";
    for (int i = L - 1; i < R; i++)
        putchar(str[i]);
    putchar('\n');

    return 0;
}
