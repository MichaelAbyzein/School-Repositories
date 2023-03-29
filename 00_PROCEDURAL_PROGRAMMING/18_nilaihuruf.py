"""

Guru akan memberikan nilai huruf ke siswa dengan
aturan sebagai berikut
A >= 90
B >= 75
C >= 65
D >= 50
F

"""
print("Hallo,")
n = float(input("Sebutkan nilainya: "))
#bottom to top
if n < 50:
    print("Nilai,", n, "adalah: F")
elif n < 65:
    print("Nilai,", n, "adalah: D")
elif n < 75:
    print("Nilai,", n, "adalah: C")
elif n < 90:
    print("Nilai,", n, "adalah: B")
else:
    print("Nilai,", n, "adalah: A")
#top to bottom
if n >= 90:
    print("Nilai,", n, "adalah: A")
elif n >= 75:
    print("Nilai,", n, "adalah: B")
elif n >= 65:
    print("Nilai,", n, "adalah: C")
elif n >= 90:
    print("Nilai,", n, "adalah: D")
else:
    print("Nilai,", n, "adalah: F")