D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
# print(pc)

ans = []
for mask in range(1 << D):
    score = 0
    used = 0
    # ビットマスクで全問回答すると選択した問題をすべて回答して、点数と回答数を加算
    for i in range(D):
        if (mask >> i) & 1:
            score += 100 * (i + 1) * pc[i][0] + pc[i][1]
            used += pc[i][0]

    # この時点で点数がG以上なら次のループへ
    if score >= G:
        ans.append((score, used))
        continue

    # Gに届かない文を高い得点の問題から貪欲に埋める（ボーナスをもらえない範囲で）
    need = G - score  # あと何点必要か？
    for i in reversed(range(D)):
        # 全問回答した問題はパスする
        if (mask >> i) & 1:
            continue

        # ボーナスをもらえない範囲で全部回答してもneedに満たなければパス
        max_take = pc[i][0] - 1  # -i としていたのを修正
        v = 100 * (i + 1)
        if v * max_take < need:
            continue

        # needを満たす最小限の問題数を求める
        take = -(-need // v)  # 天井関数
        score += v * take
        used += take
        ans.append((score, used))

# print(ans)
print(min(a for _, a in ans))

"""
ビット全探索

ざっくり言うと「bit全探索 + 貪欲での穴埋め」です。
ポイントは「ボーナスは“全部解いたとき”しか入らない」ので、
“全部解く集合”をまず決め打ちし、足りない分を高得点問題から貪欲に埋める、
という二段構えにします。

1.「全問解く種類の集合」を bitmask で全探索
2.マスクで得た得点を score とし、まだ G に届かないなら“残りの種類”から貪欲に追加
3.こうして達成できたら、そのときの 解答数の最小値を更新。
4.すべてのマスクに対して試し、最小解答数が答え。
"""
