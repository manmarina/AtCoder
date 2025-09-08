S = input().strip()

need = 'i'           # 現在欲しい文字
ins = 0              # 挿入回数
for c in S:
    if c != need:  # 違ったら1つ挿入してneedを反転
        ins += 1
        need = 'o' if need == 'i' else 'i'
    # needを反転 if文で反転してたら、反転の反転で同じneedになる
    need = 'o' if need == 'i' else 'i'

# 偶数長にするための末尾調整
# need=='o' なら今の長さは奇数なので 'o' を1つ挿入
if need == 'o':
    ins += 1

print(ins)
