#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char S[11];
    scanf("%s", S);

    // 文字列長チェック
    if (strlen(S) != 8)
    {
        puts("No");
        return 0;
    }

    char prefix = S[0];
    char suffix = S[7]; // 末尾は8文字目（インデックス7）

    // 先頭が英大文字か
    if (!isupper((unsigned char)prefix))
    {
        puts("No");
        return 0;
    }
    // 末尾が英大文字か
    if (!isupper((unsigned char)suffix))
    {
        puts("No");
        return 0;
    }
    // 中間6桁が数字か
    for (int i = 1; i <= 6; i++)
    {
        if (!isdigit((unsigned char)S[i]))
        {
            puts("No");
            return 0;
        }
    }
    // 数値に変換して 100000 以上か
    char number[7];
    strncpy(number, S + 1, 6);
    number[6] = '\0';
    if (atoi(number) < 100000)
    {
        puts("No");
        return 0;
    }

    puts("Yes");
    return 0;
}
