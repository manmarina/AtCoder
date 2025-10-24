N = int(input())
A = [0] + list(map(int, input().split()))  # 1-indexed

dic = {1: 0}  # key=アメーバの番号, value=アメーバの階層
for i in range(1, N + 1):
    dic[2 * i] = dic[A[i]] + 1  # 子の番号は、親の番号ではなく、観察記録の番号から決める
    dic[2 * i + 1] = dic[A[i]] + 1  # 子の階層は親の階層+1
# print(dic)

print(*dic.values(), sep='\n')

"""
問題文の理解が難解系

A[i]の子は、2*A[i]と2*A[i]+1ではなく、2*iと2*i+1
子の番号は、親の番号ではなく、観察記録の番号から決める
これが理解できれば、出力例2の意味がわかる
けんちょんの解法の図で理解できた
https://drken1215.hatenablog.com/entry/2023/06/07/234600
https://programming-hiroba.com/abc274-c/

https://atcoder.jp/contests/abc274/tasks/abc274_c
"""
