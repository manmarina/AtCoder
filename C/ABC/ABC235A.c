#include <stdio.h>

int main(void)
{
    char abc[4];       // 3文字 + 終端 '\0'
    scanf("%3s", abc); // 最大3文字読み込み

    int num1 = (abc[0] - '0') * 100 + (abc[1] - '0') * 10 + (abc[2] - '0');
    int num2 = (abc[1] - '0') * 100 + (abc[2] - '0') * 10 + (abc[0] - '0');
    int num3 = (abc[2] - '0') * 100 + (abc[0] - '0') * 10 + (abc[1] - '0');

    printf("%d\n", num1 + num2 + num3);

    return 0;
}
