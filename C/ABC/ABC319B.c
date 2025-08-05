#include <stdio.h>
#include <string.h>

int main()
{
    int N;
    scanf("%d", &N);

    int j[10] = {0};
    int j_count = 0;
    for (int i = 1; i <= N; i++)
    {
        if (N % i == 0 && i <= 9)
        {
            j[j_count++] = i;
        }
    }

    for (int i = 0; i <= N; i++)
    {
        int found = 0;
        for (int k = 0; k < j_count; k++)
        {
            if (i % (N / j[k]) == 0)
            {
                printf("%d", j[k]);
                found = 1;
                break;
            }
        }
        if (!found)
        {
            putchar('-');
        }
    }
    putchar('\n');

    return 0;
}
