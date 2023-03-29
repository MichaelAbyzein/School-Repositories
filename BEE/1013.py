s, m, t = input().split(" ")
s, m, t = int(s), int(m), int(t)
grea = (s+m+abs(s-m))/2
grea = int(grea)
res = (grea+t+abs(grea-t))/2
print(f"{res:.0f} eh o maior")