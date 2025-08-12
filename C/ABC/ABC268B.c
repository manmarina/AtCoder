#include <stdio.h>
#include <string.h>

int main(void)
{
    char S[101], T[101]; // 入力は最大100文字程度と仮定
    scanf("%100s", S);
    scanf("%100s", T);

    // S の長さ分だけ T の先頭と比較
    if (strncmp(T, S, strlen(S)) == 0)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
