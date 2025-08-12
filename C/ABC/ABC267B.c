#include <stdio.h>
#include <string.h>

int main(void)
{
    char buf[16]; // buf[1]〜buf[10]を使う。buf[0]はダミー
    buf[0] = '?';
    if (scanf("%15s", buf + 1) != 1)
        return 0;

    // ピン1が立っていたら即No
    if (buf[1] == '1')
    {
        puts("No");
        return 0;
    }

    // 7列の判定用文字列 line を作る
    char line[8];
    line[0] = (buf[7] == '1') ? 'o' : 'x';
    line[1] = (buf[4] == '1') ? 'o' : 'x';
    line[2] = (buf[2] == '1' || buf[8] == '1') ? 'o' : 'x';
    line[3] = (buf[5] == '1') ? 'o' : 'x';
    line[4] = (buf[9] == '1' || buf[3] == '1') ? 'o' : 'x';
    line[5] = (buf[6] == '1') ? 'o' : 'x';
    line[6] = (buf[10] == '1') ? 'o' : 'x';
    line[7] = '\0';

    const char *check[] = {"oxo", "oxxo", "oxxxo", "oxxxxo", "oxxxxxo"};
    for (int i = 0; i < 5; i++)
    {
        if (strstr(line, check[i]) != NULL)
        {
            puts("Yes");
            return 0;
        }
    }
    puts("No");
    return 0;
}
