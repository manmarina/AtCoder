#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    if (N < 126)
    {
        printf("4\n");
    }
    else if (N < 212)
    {
        printf("6\n");
    }
    else
    {
        printf("8\n");
    }

    return 0;
}
