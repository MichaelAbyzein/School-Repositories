
def print_choice():
    print("Choice : ")
    print("c - Convert to Celcius")
    print("f - Convert to Farehneit")
    print("q - Quit the Program")
    
def c_to_f(temp_c):
    return 9.0 / 5.0 * temp_c + 32

def f_to_c(temp_f):
    return (temp_f - 32) * 5.0 / 9.0

choice = None

while choice != 'q' and 'Q':

    print_choice()
    choice = input("Choice : ")
    
    if choice == "c" and "C":
        main_c = float(input("The Temperature : "))
        res = c_to_f(main_c)
        print(f"Farenheit : {res}")
    elif choice == "f" and "F":
        main_f = float(input("The Temperature :"))
        print(f"Celcius : {f_to_c(main_f)}")