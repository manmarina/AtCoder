#include <stdio.h>

int recursive(int x)
{
    if (x == 1 || x == 0)
        return 1;
    else
        return x * recursive(x - 1);
}

int main()
{
    int N;
    scanf("%d", &N);

    printf("%d\n", recursive(N));

    return 0;
}
