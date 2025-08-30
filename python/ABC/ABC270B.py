X, Y, Z = map(int, input().split())

# 座標4つの並びは4P4だが、左右対処なので、Y<0に固定すると4P4の半分で12通り
if Y < 0:
    X, Y, Z = -X, -Y, -Z

if X < Y:  # ゴールが壁の手前
    print(abs(X))
elif Y < Z:  # ハンマーが壁の奥
    print(-1)
else:  # ゴールと反対方向にハンマーを拾いに行ってからゴール
    print(abs(Z) + abs(X - Z))
