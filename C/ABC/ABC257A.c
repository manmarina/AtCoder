#include <stdio.h>

int main()
{
    int N, X;
    scanf("%d %d", &N, &X);

    int index = 65 + X / N + ((X % N) ? 1 : 0) - 1;
    printf("%c\n", (char)index);

    return 0;
}
