#include <stdio.h>
#include <string.h>

int main(void)
{
    int N;
    char S[1001];
    char replaced[2001];

    scanf("%d", &N);
    scanf("%s", S);

    int i = 0, j = 0;
    while (S[i] != '\0')
    {
        if (S[i] == 'n' && S[i + 1] == 'a')
        {
            replaced[j++] = 'n';
            replaced[j++] = 'y';
            replaced[j++] = 'a';
            i += 2; // "na" を読み飛ばす
        }
        else
        {
            replaced[j++] = S[i++];
        }
    }
    replaced[j] = '\0';

    printf("%s\n", replaced);

    return 0;
}
