#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    printf("%04d\n", N); // 4桁、足りない桁は0で埋める
    return 0;
}
