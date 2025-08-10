#include <stdio.h>

int main(void)
{
    int S, T, X;
    scanf("%d %d %d", &S, &T, &X);

    if (S < T)
    {
        if (S <= X && X < T)
            printf("Yes\n");
        else
            printf("No\n");
    }
    else
    {
        if (T <= X && X < S)
            printf("No\n");
        else
            printf("Yes\n");
    }

    return 0;
}
