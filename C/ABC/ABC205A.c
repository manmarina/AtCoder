#include <stdio.h>

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    // 100で割るので小数が出る可能性があるためdouble型にキャスト
    printf("%f\n", (double)A * B / 100);

    return 0;
}
