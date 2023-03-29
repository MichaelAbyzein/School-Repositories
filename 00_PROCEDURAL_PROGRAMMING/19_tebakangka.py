from random import randint
import os

os.system("cls") # screen swiper (hapus text sebelum file ini dijalankan)

benar = randint(0, 10) # a to b (ex. 1 to 255)
tebak = None

while tebak != benar:
    tebak = int(input("Angka Tebakannya = "))
    
    if tebak == benar:
        print("Ya, anda benar!")
    
    elif tebak > benar:
        print(f"Angkanya lebih kecil dari {tebak}")
        
    elif tebak < benar:
        print(f"Angkanya lebih besar dari {tebak}")
# "f" untuk memasukan variable dalam "{}".