#include <stdio.h>

int main(void)
{
    long long N;
    scanf("%lld", &N);

    if (N >= -(1LL << 31) && N < (1LL << 31))
        printf("Yes\n");
    else
        printf("No\n");

    return 0;
}
