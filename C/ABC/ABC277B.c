#include <stdio.h>
#include <string.h>

int main(void)
{
    int N;
    if (scanf("%d", &N) != 1)
        return 0;

    char S[52][3]; // 各カードは2文字＋終端
    const char *check1 = "HDCS";
    const char *check2 = "A23456789TJQK";

    for (int i = 0; i < N; i++)
    {
        char buf[3];
        scanf("%s", buf);

        // 1文字目(スート)と2文字目(ランク)の妥当性チェック
        if (strchr(check1, buf[0]) == NULL || strchr(check2, buf[1]) == NULL)
        {
            puts("No");
            return 0;
        }

        // 保存（比較用に厳密に2文字だけ保持）
        S[i][0] = buf[0];
        S[i][1] = buf[1];
        S[i][2] = '\0';
    }

    // 重複チェック（O(N^2)で十分）
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            if (strcmp(S[i], S[j]) == 0)
            {
                puts("No");
                return 0;
            }
        }
    }

    puts("Yes");
    return 0;
}
