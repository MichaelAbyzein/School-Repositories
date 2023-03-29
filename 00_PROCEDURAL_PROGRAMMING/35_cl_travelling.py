"""
1. Bayangkan kalian akan pergi ke 5 destinasi wisata
2. Buatkan list dari 5 tempat tersebut dan tidak perlu terurut
3. Cetak list original
4. Cetak list terurut tanpa mengubah list yang asli
5. Karena dana terbatas hapus 2 tujuan, yg pertama hapus item di index 3, yg kedua hapus di index terakhir
6. Tiba-tiba ada sponsor yang mendanai ke paris, masukan paris ke tujuan pertama di lists
7. Cetak lists setelah permanen dan secara menurun
Cl ini dikumpul di moodle menggunakan link pastebin 

"""

vac_list = ["Tokyo", "Auckland", "London", "Berlin", "Bali"]
print(vac_list)
print(sorted(vac_list))

del vac_list[-1 and 3]
print(vac_list)

vac_list.insert(0, "Paris")
print(vac_list)

vac_list.sort(reverse=True)
print(vac_list)