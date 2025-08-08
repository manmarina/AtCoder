#include <stdio.h>

int main(void)
{
    int V;
    int ABC[3] = {0, 0, 0}; // Pythonの [0, 0, 0] 相当

    // V, ABC[0], ABC[1], ABC[2] をまとめて読み込み
    scanf("%d%d%d%d", &V, &ABC[0], &ABC[1], &ABC[2]);

    while (1)
    {
        for (int i = 0; i < 3; i++)
        {
            V -= ABC[i];
            if (V < 0)
            {
                if (i == 0)
                    printf("F\n");
                else if (i == 1)
                    printf("M\n");
                else
                    printf("T\n");

                return 0; // exit()
            }
        }
    }

    return 0;
}
