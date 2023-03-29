"""

Indri ingin pulang sekolah dengan ongkos sebanyak 5000
dengan situasi kendaraan sebagai berikut.

Taksi: 45_000
Ojek : 25_000
Becak : 15_000
Angkot: 5_000
Sikil : 2_000

"""

UI = float(input("Berapa uangnya: "))
#bottom to top
if UI < 5000:
    print("Jalan Kaki Saja")
elif UI < 15000:
    print("Angkot Aja...")
elif UI < 25000:
    print("becak asyik ni")
elif UI < 45000:
    print("Cepat kalau naik ojek")
else:
    print("Naik Taksi")

#top to bottom
if UI >= 45000:
    print("Naik Taksi")
elif UI >= 25000:
    print("Cepat kalo naik ojek")
elif UI >= 15000:
    print("Becak asyik ni")
elif UI >= 5000:
    print("Angkot Aja...")
else:
    print("Jalan Kaki Saja")
