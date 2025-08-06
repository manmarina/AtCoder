#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);

    int A[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    int sum = 0;
    for (int i = 0; i < N; i++)
        sum += A[i];

    printf("%d\n", sum);

    return 0;
}
