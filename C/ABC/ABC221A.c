#include <stdio.h>
#include <math.h>

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);

    printf("%.0f\n", pow(32, A - B));

    return 0;
}
