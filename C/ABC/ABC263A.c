#include <stdio.h>

int compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    int S[5];
    for (int i = 0; i < 5; i++)
        scanf("%d", &S[i]);

    qsort(S, 5, sizeof(int), compare);

    if ((S[0] == S[1] && S[2] == S[3] && S[3] == S[4]) ||
        (S[0] == S[1] && S[1] == S[2] && S[3] == S[4]))
        puts("Yes");
    else
        puts("No");

    return 0;
}
