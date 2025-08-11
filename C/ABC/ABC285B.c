#include <stdio.h>
#include <string.h>

int main(void)
{
    int N;
    char S[5001]; // 入力の最大長に応じてサイズを調整

    scanf("%d", &N);
    scanf("%s", S);

    for (int i = 0; i < N - 1; i++)
    {
        int count = 0;
        int broken = 0; // break したかどうか

        for (int j = i + 1; j < N; j++)
        {
            if (S[j - i - 1] != S[j])
            {
                count++;
            }
            else
            {
                printf("%d\n", count);
                broken = 1;
                break;
            }
        }
        if (!broken)
        {
            printf("%d\n", count);
        }
    }

    return 0;
}
