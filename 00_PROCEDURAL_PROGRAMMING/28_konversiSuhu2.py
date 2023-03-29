import os

def print_choice():
    print("Temperature Convertion")
    
    print("Convertion Choice : ")
    
    print("cf - Celcius to Farenheit")
    print("cr - Celcius to Reamur")
    print("ck - Celcius to Kelvin")
    print("fc - Farenheit to Celcius")
    print("fr - Farenheit to Reamur")
    print("fk - Farenheit to Kelvin")
    print("rc - Reamur to Celcius")
    print("rf - Reamur to Farenheit")
    print("rk - Reamur to Kelvin")
    print("kc - Kelvin to Celcius")
    print("kf - Kelvin to Farenheit")
    print("kr - Kelvin to Reamur")
    
    print("q - Quit the Program")
    
#C:R:F:K = 5:4:9(+= 32):5(+-273)
    
def c_to_f(temp_c):
    return 9.0 / 5.0 * temp_c + 32

def f_to_c(temp_f):
    return (temp_f - 32) * 5.0 / 9.0
    
def c_to_r(temp_c):
    return 4.0 / 5.0 * temp_c
    
def f_to_r(temp_f):
    return 4.0 / 9.0 * (temp_f-32)
    
def c_to_k(temp_c):
    return temp_c + 273
    
def f_to_k(temp_f):
    return (temp_f - 32) * 5.0 / 9.0 + 273

def r_to_c(temp_r):
    return 5.0 / 4.0 * temp_r

def r_to_f(temp_r):
    return 9.0 / 4.0 * temp_r + 32
    
def r_to_k(temp_r):
    return 5.0 / 4.0 * temp_r + 273
    
def k_to_c(temp_k):
    return temp_k - 273
    
def k_to_f(temp_k):
    return (temp_k - 273) * 9.0 / 5.0 + 32
    
def k_to_r(temp_k):
    return (temp_k - 273) * 4.0 / 5.0

running = True
choice = None

while running:
    os.system("cls")
    print_choice()
    choice = input("Choice : ")
    
    if choice == "cf":
        main_c = float(input("The Temperature : "))
        result = c_to_f(main_c)
        print(f"Farenheit : {result}")
        
        input("Press Enter to Main Menu")
        
    if choice == "fc":
        main_f = float(input("The Temperature :"))
        print(f"Celcius : {f_to_c(main_f)}")
        
        input("Press Enter to Main Menu")
    
    if choice == "cr":
        main_c = float(input("The Temperature : "))
        result = c_to_r(main_c)
        print(f"Reamur : {result}")
        
        input("Press Enter to Main Menu")
        
    if choice == "fr":
        main_f = float(input("The Temperature :"))
        print(f"Reamur : {f_to_r(main_f)}")
        
        input("Press Enter to Main Menu")

    if choice == "ck":
        main_c = float(input("The Temperature : "))
        result = c_to_k(main_c)
        print(f"Kelvin : {result}")
        
        input("Press Enter to Main Menu")
        
    if choice == "fk":
        main_f = float(input("The Temperature :"))
        print(f"Kelvin : {f_to_k(main_f)}")
        
        input("Press Enter to Main Menu")
    
    if choice == "rc":
        main_r = float(input("The Temperature : "))
        result = r_to_c(main_r)
        print(f"Celcius : {result}")
        
        input("Press Enter to Main Menu")
        
    if choice == "rf":
        main_r = float(input("The Temperature :"))
        print(f"Farenheit : {r_to_f(main_r)}")
        
        input("Press Enter to Main Menu")
    
    if choice == "rk":
        main_r = float(input("The Temperature : "))
        result = r_to_k(main_r)
        print(f"Kelvin : {result}")
        
        input("Press Enter to Main Menu")
        
    if choice == "kc":
        main_k = float(input("The Temperature :"))
        print(f"Celcius: {k_to_c(main_k)}")
        
        input("Press Enter to Main Menu")
    
    if choice == "kf":
        main_k = float(input("The Temperature : "))
        result = k_to_f(main_k)
        print(f"Farenheit : {result}")
        
        input("Press Enter to Main Menu")
        
    if choice == "kr":
        main_k = float(input("The Temperature :"))
        print(f"Reamur : {k_to_r(main_k)}")
        
        input("Press Enter to Main Menu")
        
    elif choice == 'q':
        running = False
        os.system("cls")
        print("Goodbye, See You Soon!")