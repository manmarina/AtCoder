N = int(input())
SF = []
for i in range(N):
    f, s = map(int, input().split())
    SF.append((s, f))
# print(SF)

SF.sort(reverse=True)  # 　おいしさの大きい順にソート
# print(SF)


ans = [SF[0][0]]  # おいしさが一番大きいものを食べる。
if SF[0][1] == SF[1][1]:  # 次に大きいものが、最初に食べたものと同じ味なら
    for i in range(2, N):
        if SF[1][1] == SF[i][1]:  # 最初に食べたものと別の味のもので、一番大きいものを探す
            continue
        else:  # 見つかったら、
            ans.append(max(SF[1][0] // 2, SF[i][0]))  # 大きい方を食べる。
            break
else:  # そうでなければ
    ans.append(SF[1][0])  # 次に大きいものを食べる

# print(ans)
print(sum(ans))

"""
WA

おいしさの大きい順にソート。
おいしさが一番大きいものを食べる。
もう一つは、次に大きいものが、最初に食べたものと同じ味なら、おいしさを1/2(=A)にする。
最初に食べたものと別の味のもので、一番大きいものを探し、Aと比較。
大きい方を食べる。

https://atcoder.jp/contests/abc315/tasks/abc315_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6902281a-d554-8321-85bb-942af7e0400e
"""
