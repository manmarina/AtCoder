#include <stdio.h>

int main(void)
{
    long long N;
    scanf("%lld", &N);

    long long mod = 998244353;
    long long ans = N % mod;
    if (ans < 0)
        ans += mod;

    printf("%lld\n", ans);
    return 0;
}
