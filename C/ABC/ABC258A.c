#include <stdio.h>

int main()
{
    int K;
    scanf("%d", &K);

    int base_hour = 21;
    int base_minute = 0;

    int total_minutes = base_hour * 60 + base_minute + K;
    int result_hour = (total_minutes / 60) % 24;
    int result_minute = total_minutes % 60;

    printf("%02d:%02d\n", result_hour, result_minute);

    return 0;
}
