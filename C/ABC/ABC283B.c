#include <stdio.h>
#include <stdint.h>

int main(void)
{
    int N, M;
    if (scanf("%d %d", &N, &M) != 2)
        return 0;

    uint32_t mask[30] = {0}; // N ≤ 30
    char s[31];              // 文字列長 M ≤ 30（+終端）

    for (int i = 0; i < N; i++)
    {
        scanf("%s", s);
        uint32_t m = 0;
        for (int j = 0; j < M; j++)
        {
            if (s[j] == 'o')
                m |= (1u << j);
        }
        mask[i] = m;
    }

    uint32_t full = (1u << M) - 1u;
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if ((mask[i] | mask[j]) == full)
            {
                count++;
            }
        }
    }

    printf("%d\n", count);
    return 0;
}
