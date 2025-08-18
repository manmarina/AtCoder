s1 = "cbaa"
s2 = "daacc"
s3 = "acacac"


def count_chars(s):
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d


# 各文字列の出現回数をカウント
d1 = count_chars(s1)
d2 = count_chars(s2)
d3 = count_chars(s3)
print(d1)
print(d2)
print(d3)

# 共通部分を求める
result = []
for ch in d1:
    if ch in d2 and ch in d3:
        common_count = min(d1[ch], d2[ch], d3[ch])
        result.extend([ch] * common_count)

# 辞書順に並べる
result.sort()

# 文字列化
answer = "".join(result)
print(answer)   # aac
