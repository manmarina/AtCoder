def read_shape(N, grid):  # '#'の座標を格納したリストを返す関数
    pts = [(r, c) for r in range(N) for c in range(N) if grid[r][c] == '#']
    return pts


def normalize(pts):  # 座標を(0,0)を基準として変更（正規化）する関数
    if not pts:
        return frozenset()  # 図形なし
    min_r = min(r for r, _ in pts)
    min_c = min(c for _, c in pts)
    return frozenset((r - min_r, c - min_c) for r, c in pts)
    # イミュータブルなfrozenset型を使用しているが、今回の場合はsetでも問題なく動作する。


def rotate90_origin(pts):  # 座標を90°右に回転する関数
    # (x, y) -> (y, -x)
    return [(c, -r) for r, c in pts]


N = int(input())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(N)]

s_pts = read_shape(N, S)  # Sの'#'の座標を格納したリスト
t_pts = read_shape(N, T)  # Tの'#'の座標を格納したリスト
# print(s_pts)
# print(t_pts)

# SとTで'#'の数が異なったら終了
if len(s_pts) != len(t_pts):
    print("No")
    exit()

# Sの座標を(0,0)を基準として変更（正規化）
s_norm = normalize(s_pts)
# print(s_norm)

# 正規化したSと正規化したTを4回転照合する
cur = t_pts
for _ in range(4):
    t_norm = normalize(cur)  # Tは回転する事に再度正規化する
    if t_norm == s_norm:
        print("Yes")
        exit()
    # 次の回転へ
    cur = rotate90_origin(cur)  # Tを90°回転する
    # t_normはfrozenset型なので、回転させるためにはリストに戻さなければならない。
    # それを避けるためにcurを回転してそれを正規化している

print("No")

"""
カーソル系（グリッド走査）
チャッピー

2つの NxN グリッド S と T に描かれた '#’ 図形が、
90°回転（0/90/180/270°のいずれか）+平行移動で一致するかを判定する実装問題です。

必要なテクニック・アルゴリズム
座標取り出し
    '#' の位置座標集合 P = {(r,c)} を作ります。
    最初に '#' の個数が等しいかをチェック（異なれば絶対一致しない）。

平行移動の吸収（正規化）
    図形の左上端に原点を合わせると、平行移動の影響を消せます。
    具体的には、min_r = min(r), min_c = min(c) を求め、
    P_norm = {(r-min_r, c-min_c)} に変換。
    これで「左上が(0,0)」な形の表現になります。

回転の吸収
回転は4通りだけ試せば十分。座標の回転は次のいずれかで：
    原点回り 90°回転： (x, y) → (y, -x)
    180°： (x, y) → (-x, -y)
    270°： (x, y) → (-y, x)
    ※この「原点回り」回転を使うなら、毎回②の正規化（左上合わせ）をやり直せば OK（負座標が出ても正規化で吸収）。
    あるいはグリッド内回転（(r,c)→(c, N-1-r) など）でも良いですが、毎回 N に依存して少し煩雑。
    上の“原点回り回転→再正規化”の方が実装が楽です。

集合として比較
    S の正規化済み集合と、T の各回転→正規化集合を set 比較（もしくはソート済みリスト比較）します。
    どれか一致すれば “Yes”、全部ダメなら “No”。
"""
