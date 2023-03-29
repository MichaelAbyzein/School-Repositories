#list kosong untuk aliens
aliens = []

#buat 30 alien hijau
for i in range(30):
    alien = {'color': 'green', 'points':0}
    aliens.append(alien)
    
#menampilkan 5 alien di awal
for alien in aliens[0:5]: #aliens[:5]
    print(alien)
    
#mengetahui jumlah item dalam  list
print(f"Total number of aliens is {len(aliens)}")