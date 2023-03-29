N1, N2, N3, N4 = map(float, input().split())

avrg = (2*N1+3*N2+4*N3+1*N4)/10


if avrg >= 7:
	print(f"Media: {avrg:.1f}")
	print("Aluno aprovado.")
elif avrg >=5:
	rs = float(input())
	print(f"Media: {avrg:.1f}")
	print("Aluno em exame.")
	print(f"Nota do exame: {rs}")
	print("Aluno aprovado.")
	print(f"Media final: {(avrg+rs)/2}")
else:
	print(f"Media: {avrg:.1f}")
	print("Aluno reprovado.")