#include <stdio.h>
#include <string.h>

int main()
{
    char *name[] = {"tourist", "ksun48", "Benq", "Um_nik", "apiad",
                    "Stonefeang", "ecnerwala", "mnbvmar", "newbiedmy", "semiexp"};
    int score[] = {3858, 3679, 3658, 3648, 3638,
                   3630, 3613, 3555, 3516, 3481};

    char S[20];
    scanf("%s", S);

    int n = sizeof(score) / sizeof(score[0]);
    for (int i = 0; i < n; i++)
    {
        if (strcmp(name[i], S) == 0)
        {
            printf("%d\n", score[i]);
            return 0;
        }
    }

    return 0;
}
