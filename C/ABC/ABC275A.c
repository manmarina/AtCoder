#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);

    int H[N];
    for (int i = 0; i < N; i++)
        scanf("%d", &H[i]);

    int max = 0;
    int index = 0;
    for (int i = 0; i < N; i++)
    {
        if (H[i] > max)
        {
            max = H[i];
            index = i + 1;
        }
    }
    printf("%d\n", index);

    return 0;
}
