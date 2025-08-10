#include <stdio.h>

int f(int t)
{
    return t * t + 2 * t + 3;
}

int main(void)
{
    int t;
    scanf("%d", &t);

    printf("%d\n", f(f(f(t) + t) + f(f(t))));

    return 0;
}
