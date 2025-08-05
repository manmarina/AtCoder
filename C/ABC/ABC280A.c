#include <stdio.h>

int main()
{
    int H, W;
    scanf("%d%d", &H, &W);

    char S[H][W + 1];
    for (int i = 0; i < H; i++)
        scanf("%s", S[i]);

    int count = 0;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++)
        {
            if (S[i][j] == '#')
                count++;
        }

    printf("%d\n", count);

    return 0;
}
