#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int ABCD[100][4]; // 最大100個の長方形を格納 (A,B,C,D)
    for (int i = 0; i < N; i++)
    {
        scanf("%d %d %d %d", &ABCD[i][0], &ABCD[i][1], &ABCD[i][2], &ABCD[i][3]);
    }

    int count = 0;
    for (int x = 0; x < 100; x++)
    {
        for (int y = 0; y < 100; y++)
        {
            for (int i = 0; i < N; i++)
            {
                int A = ABCD[i][0];
                int B = ABCD[i][1];
                int C = ABCD[i][2];
                int D = ABCD[i][3];
                if (A <= x && x < B && C <= y && y < D)
                {
                    count++;
                    break; // 最初にヒットしたら次の(x,y)へ
                }
            }
        }
    }

    printf("%d\n", count);

    return 0;
}
