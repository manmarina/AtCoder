#include <stdio.h>

int main(void)
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);

    int ans = -1;
    int calc = C * ((A / C) + 1);

    if (A % C == 0)
    {
        ans = A;
    }
    else if (A <= calc && calc <= B)
    {
        ans = calc;
    }

    printf("%d\n", ans);
    return 0;
}
