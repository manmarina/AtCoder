#include <stdio.h>
#include <stdlib.h>

// 比較関数（昇順）
int compare_int(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    int abc[3];
    scanf("%d%d%d", &abc[0], &abc[1], &abc[2]);

    int sorted[3];
    for (int i = 0; i < 3; i++)
    {
        sorted[i] = abc[i]; // 元の順序を保持したい場合にコピー
    }

    qsort(sorted, 3, sizeof(int), compare_int);

    int median = sorted[1]; // 中央の値

    if (abc[1] == median)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
