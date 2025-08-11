#include <stdio.h>

int main(void)
{
    const long long MOD = 998244353;

    long long A, B, C, D, E, F;
    if (scanf("%lld %lld %lld %lld %lld %lld", &A, &B, &C, &D, &E, &F) != 6)
        return 0;

    // 各値を先に MOD に落とす
    long long a = A % MOD, b = B % MOD, c = C % MOD;
    long long d = D % MOD, e = E % MOD, f = F % MOD;

    // (a*b)%MOD は最大でも ~1e18 なので long long の範囲に収まる
    long long lhs = (((a * b) % MOD) * c) % MOD; // A*B*C % MOD
    long long rhs = (((d * e) % MOD) * f) % MOD; // D*E*F % MOD

    long long ans = lhs - rhs;
    if (ans < 0)
        ans += MOD; // Cの%は負になり得るので補正

    printf("%lld\n", ans);
    return 0;
}
