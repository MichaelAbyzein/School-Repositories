va, vb, vc = input().split(" ")
va, vb, vc = float(va), float(vb), float(vc)
tri = 1 / 2 * va * vc
cir = 3.14159 * vc**2
tra = 1 / 2 * (va + vb) * vc
squ = vb**2
rec = va * vb
print(f"""TRIANGULO: {tri:.3f}
CIRCULO: {cir:.3f}
TRAPEZIO: {tra:.3f}
QUADRADO: {squ:.3f}
RETANGULO: {rec:.3f}""")