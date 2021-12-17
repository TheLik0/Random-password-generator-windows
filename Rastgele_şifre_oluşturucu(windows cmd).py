from os import system
system("cls")
system("color a")

print("░██████╗██╗███████╗██████╗░███████╗")
print("██╔════╝██║██╔════╝██╔══██╗██╔════╝")
print("╚█████╗░██║█████╗░░██████╔╝█████╗░░")
print("░╚═══██╗██║██╔══╝░░██╔══██╗██╔══╝░░")
print("██████╔╝██║██║░░░░░██║░░██║███████╗")
print("╚═════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝")
print("    ")
print("░█████╗░██╗░░░░░██╗░░░██╗░██████╗████████╗██╗░░░██╗██████╗░██╗░░░██╗░█████╗░██╗░░░██╗")
print("██╔══██╗██║░░░░░██║░░░██║██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██║░░░██║██╔══██╗██║░░░██║")
print("██║░░██║██║░░░░░██║░░░██║╚█████╗░░░░██║░░░██║░░░██║██████╔╝██║░░░██║██║░░╚═╝██║░░░██║")
print("██║░░██║██║░░░░░██║░░░██║░╚═══██╗░░░██║░░░██║░░░██║██╔══██╗██║░░░██║██║░░██╗██║░░░██║")
print("╚█████╔╝███████╗╚██████╔╝██████╔╝░░░██║░░░╚██████╔╝██║░░██║╚██████╔╝╚█████╔╝╚██████╔╝")
print("░╚════╝░╚══════╝░╚═════╝░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░░╚═════╝░")
print("code writed by lik0")
print("    ")
uzunluk = input('şifrenizin kaç haneli olucağını seçiniz(max 15) : ')

if(int(uzunluk)>15):
    print("lütfen geçerli bir değer giriniz")
    from os import system
    import time
    time.sleep(3)
    system("cls")
    import sys
    sys.exit()
if(int(uzunluk)==1):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 1
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==2):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 2
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==3):  

    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 3
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==4):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 4
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==5):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 5
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==6):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 6
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==7):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 7
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==8):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 8
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==9):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 9
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==10):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 10
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==11):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 11
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==12):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 12
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==13):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 13
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==14):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 14
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 
if(int(uzunluk)==15):
    import random
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIİJKLMOÖPRSŞTUÜVYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}#()*;._-"

    all=lower + upper + NUMBER + Symbol
    lenght = 15
    password = "".join(random.sample(all,lenght))
    print(" Rastgele şifren : ",password) 