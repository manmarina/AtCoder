#include <stdio.h>

int main()
{
    int L1, R1, L2, R2;
    scanf("%d%d%d%d", &L1, &R1, &L2, &R2);

    int L_max = L1;
    if (L1 < L2)
        L_max = L2;

    int R_min = R1;
    if (R1 > R2)
        R_min = R2;

    int length = R_min - L_max;
    if (length < 0)
        length = 0;

    printf("%d\n", length);

    return 0;
}
