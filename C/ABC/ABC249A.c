#include <stdio.h>

int distance(int run, int speed, int rest, int total_time)
{
    int dist = 0;
    while (total_time > 0)
    {
        if (total_time >= run)
        {
            dist += run * speed;
            total_time -= run + rest;
        }
        else
        {
            dist += total_time * speed;
            break;
        }
    }
    return dist;
}

int main()
{
    int A, B, C, D, E, F, X;
    scanf("%d%d%d%d%d%d%d", &A, &B, &C, &D, &E, &F, &X);

    int takahashi = distance(A, B, C, X);
    int aoki = distance(D, E, F, X);

    if (takahashi > aoki)
        printf("Takahashi\n");
    else if (takahashi < aoki)
        printf("Aoki\n");
    else
        printf("Draw\n");

    return 0;
}
