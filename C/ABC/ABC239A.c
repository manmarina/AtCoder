#include <stdio.h>
#include <math.h>

int main(void)
{
    int H; // 上限10^5ならintでOK
    scanf("%d", &H);

    double result = sqrt((double)H * (12800000.0 + H));
    printf("%.10f\n", result); // 誤差許容に応じて桁数調整

    return 0;
}
