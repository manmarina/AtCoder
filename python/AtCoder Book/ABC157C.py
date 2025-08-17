N, M = map(int, input().split())
sc = [tuple(map(int, input().split())) for _ in range((M))]


def check_sc(N, sc):
    # 同じ桁に違う値が来たら即終了
    ans = [None] * N
    for s, c in sc:
        s -= 1
        if ans[s] is None:
            ans[s] = c
        elif ans[s] != c:
            return None

    # 1桁でない時、1桁目が0なら即終了
    if N != 1 and ans[0] == 0:
        return None

    return ans


def convert_to_int(N, ans):
    # 1桁目のNoneを1に変換（N=1のときは0)
    if ans[0] is None:
        ans[0] = 0 if N == 1 else 1
    # その他のNoneを0に変換
    for i in range(N):
        if ans[i] is None:
            ans[i] = 0

    return int(''.join(map(str, ans)))


ans = check_sc(N, sc)
if ans is None:
    print(-1)
else:
    print(convert_to_int(N, ans))
