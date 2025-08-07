#include <stdio.h>
#include <string.h>

int main()
{
    char input[20];
    scanf("%s", input);

    int flag_input[10] = {0};                               // 入力された数字のフラグ
    int flag_template[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}; // "0"〜"9" の存在フラグ

    // 入力にある数字を記録
    for (int i = 0; i < strlen(input); i++)
    {
        if ('0' <= input[i] && input[i] <= '9')
        {
            int d = input[i] - '0';
            flag_input[d] = 1;
        }
    }

    // 対称差（XOR）を出力
    for (int i = 0; i < 10; i++)
    {
        if (flag_input[i] != flag_template[i]) // どちらかにしかない
        {
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;
}
