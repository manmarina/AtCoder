#include <stdio.h>

int main(void)
{
    int X;
    scanf("%d", &X);

    char *message = "No"; // 初期値 "No"

    if (X >= 100 && X % 100 == 0)
    {
        // "Yes" に置き換え
        message = "Yes";
    }

    printf("%s\n", message);

    return 0;
}
