#include <stdio.h>
#include <string.h>

int main()
{
    char S[10];
    scanf("%s", S);

    char *weekdays[] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    for (int i = 0; i < 5; i++)
    {
        if (strcmp(weekdays[i], S) == 0)
            printf("%d\n", 5 - i);
    }

    return 0;
}
