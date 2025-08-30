import math

a, b, d = map(float, input().split())

rad = math.radians(d)            # d * math.pi / 180.0
x = a * math.cos(rad) - b * math.sin(rad)
y = a * math.sin(rad) + b * math.cos(rad)
print(x, y)                      # 誤差許容内
# 必要なら桁数指定: print(f"{x:.10f} {y:.10f}")
