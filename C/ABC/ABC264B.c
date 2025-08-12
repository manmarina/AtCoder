#include <stdio.h>

int main(void)
{
    int R, C;
    int grid[16][16] = {0}; // 0初期化

    scanf("%d %d", &R, &C);

    // 外側
    for (int i = 1; i < 16; i++)
    {
        grid[1][i] = 1;
        grid[15][i] = 1;
        grid[i][1] = 1;
        grid[i][15] = 1;
    }

    // 2番目の枠
    for (int i = 3; i < 14; i++)
    {
        grid[3][i] = 1;
        grid[13][i] = 1;
        grid[i][3] = 1;
        grid[i][13] = 1;
    }

    // 3番目の枠
    for (int i = 5; i < 12; i++)
    {
        grid[5][i] = 1;
        grid[11][i] = 1;
        grid[i][5] = 1;
        grid[i][11] = 1;
    }

    // 一番内側の枠
    for (int i = 7; i < 10; i++)
    {
        grid[7][i] = 1;
        grid[9][i] = 1;
        grid[i][7] = 1;
        grid[i][9] = 1;
    }

    if (grid[R][C] == 1)
        printf("black\n");
    else
        printf("white\n");

    return 0;
}
