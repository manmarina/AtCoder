S = input()

name = ["tourist", "ksun48", "Benq", "Um_nik", "apiad",
        "Stonefeang", "ecnerwala", "mnbvmar", "newbiedmy", "semiexp"]
score = [3858, 3679, 3658, 3648, 3638, 3630, 3613, 3555, 3516, 3481]

player_dict = dict(zip(name, score))
print(player_dict[S])
