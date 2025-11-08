N = int(input())
WHB = [list(map(int, input().split())) for _ in range(N)]
# print(WHB)
WHB.sort(key=lambda x: -(x[2] - x[1]))
# print(WHB)

ans = []
for i in range(1, N):
    happy = 0
    head = 0
    body = 0
    for j in range(N):
        if j < i:
            happy += WHB[j][2]
            body += WHB[j][0]
        else:
            happy += WHB[j][1]
            head += WHB[j][0]
    ans.append((happy, head, body))

ans.sort(reverse=True)
print(ans)

for ha, he, bo in ans:
    if he <= bo:
        print(ha)
        exit()

"""
未完
Bi - Hi の降順にソート
境目をずらしながら境目より下は体に、上は頭に取り付ける。
全通りの中から、ギリギリ点灯しないものの嬉しさが最大値と考えたが、このロジックでは正解にならないらしい。
(入力例4の答えが得られなかった。)
"""
