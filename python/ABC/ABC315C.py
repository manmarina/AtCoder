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
    else:  # 全部同じ味のときは <- この条件を見落としがち！！！
        ans.append(SF[1][0] // 2)  # 2番目に大きいものを食べる
else:  # そうでなければ
    ans.append(SF[1][0])  # 次に大きいものを食べる

# print(ans)
print(sum(ans))

"""
場合分け系

おいしさの大きい順にソート。
おいしさが一番大きいものを食べる。
もう一つは、次に大きいものが、最初に食べたものと同じ味なら、おいしさを1/2(=A)にする。
最初に食べたものと別の味のもので、一番大きいものを探し、Aと比較。
大きい方を食べる。

チャッピーでもWAの原因が特定できなかったが、テストケースを自作して
全部同じ味のときの条件が抜けていたことが原因とわかった。

    else:  # 全部同じ味のときは <- この条件を見落としがち！！！
        ans.append(SF[1][0] // 2)  # 2番目に大きいものを食べる

プロひろの解説
https://programming-hiroba.com/abc315-c/

https://atcoder.jp/contests/abc315/tasks/abc315_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6902281a-d554-8321-85bb-942af7e0400e
"""
