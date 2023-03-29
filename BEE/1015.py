a1, b1 = input().split(" ")
a2, b2 = input().split(" ")
a1, b1, a2, b2 = float(a1), float(b1), float(a2), float(b2)
import math
dis = math.sqrt((a2-a1)**2 + (b2-b1)**2)
print(f"{dis:.4f}")