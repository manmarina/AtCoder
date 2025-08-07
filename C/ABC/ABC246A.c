#include <stdio.h>

int main(void)
{
    int X[3], Y[3];

    for (int i = 0; i < 3; i++)
    {
        scanf("%d %d", &X[i], &Y[i]);
    }

    // 同じ値が2回出る前提なら、XORで一意の値が残る
    int x3 = X[0] ^ X[1] ^ X[2];
    int y3 = Y[0] ^ Y[1] ^ Y[2];

    printf("%d %d\n", x3, y3);
    return 0;
}
