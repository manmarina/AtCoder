#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int R, C;
    if (scanf("%d %d", &R, &C) != 2)
        return 0;

    int dr = abs(R - 8);
    int dc = abs(C - 8);
    int d = (dr > dc) ? dr : dc; // Chebyshev距離

    puts((d % 2) ? "black" : "white");
    return 0;
}
