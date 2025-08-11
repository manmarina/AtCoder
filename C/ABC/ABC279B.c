#include <stdio.h>
#include <string.h>

int main(void)
{
    char S[101], T[101]; // 入力の最大長に合わせてサイズ調整

    scanf("%s", S);
    scanf("%s", T);

    if (strstr(S, T) != NULL)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
