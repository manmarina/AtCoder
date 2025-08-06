#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int main()
{
    int S[5];
    for (int i = 0; i < 5; i++)
        scanf("%d", &S[i]);

    qsort(S, 5, sizeof(int), compare);

    int count = 1;
    for (int i = 1; i < 5; i++)
    {
        if (S[i] != S[i - 1])
            count++;
    }
    printf("%d\n", count);

    return 0;
}
