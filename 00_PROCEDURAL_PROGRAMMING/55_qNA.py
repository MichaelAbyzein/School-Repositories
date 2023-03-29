import os
def scrcls():
    os.system("cls")

def s_q():

    return [
        ["What month it is during autumn?", "September"],
        ["What animal that considered a mammal and live in the ocean?", "Whale"],
        ["How tall is the statue of liberty (in Metres)?", "43"],
        ["What country located in 1° 17′ 0″ N, 103° 50′ 0″ E", "Singapore"],
        ["What 2(128*432*120)/40?", "331776"],
        ["How far does the pigeons fly (in Miles)?", "700"],
        ["What is the three letter of a mouse trap?", "Cat"],
        ["What is the largest river in Finland?", "Kemijoki"],
        ["What color is the daytime sky on a clear day?", "Blue"],
        ["What's the boiling temperature of water (in Farenheit)?", "212"]
    ] 

def c_q(r):
    que = r[0]
    ans = r[1]
                
    ent_ans = input(f"{que} ")
    if ans == ent_ans:
        print("Correct!")
        input("Press ENTER to Continue ")
        scrcls()
        return True
    else:
        print("False!")
        input("Press ENTER to Continue ")
        scrcls()
        return False

def t_st(qs):
    if len(qs) == 0:
        print("No Que Founded!")
    else:
        cor = 0
        ord = 0
        
        while ord < len(qs):
            
            #print(qs[ord])
            
         if c_q(qs[ord]):
            cor += 1
                
         ord += 1
        print(f"Your grades are {cor/len(qs)*100}")

t_st(s_q())