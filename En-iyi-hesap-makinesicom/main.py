from art import logo
from replit import clear

print(logo)
finish = False
again = False
ilk31 = False
while not finish:
    
    if not again:
        n1 = float(input("İlk Sayıyı giriniz : "))
        if n1 == 31:
            print("🤣😂🤣😂🤣😂🤣😂🤣😂🤣😂🤣😂🤣😂🤣😂")
            ilk31 = True
    
    opr = input("İşlem seçiniz '+' '-' '*' '/' \n ")
    n2 = float(input("İkinci sayıyı giriniz : "))
    if n2 == 31 and ilk31:
        print("Yeter birader mal mısın amk 31 31")
    
    def topla(n1,n2):
        return n1+n2
    def çıkar(n1,n2):
        return n1-n2
    def çarp(n1,n2):
        return n1*n2
    def böl(n1,n2):
        return n1/n2
        
    if opr == "+":
        sonuç = topla(n1,n2)
        if sonuç == 31:
            print("BGUSUFGSDFOHUDFSGHJL")
        print(f"Hesap sonucu: {sonuç}")        
    if opr == "-":
        sonuç = çıkar(n1,n2)
        if sonuç == 31:
            print("😬")
        print(f"Hesap sonucu: {sonuç}")
    if opr == "*":
        sonuç = çarp(n1,n2)
        if sonuç == 31:
            print("BGUSUFGSDFOHUDFSGHJL")
        print(f"Hesap sonucu: {sonuç}")
    if opr == "/":
        sonuç = böl(n1,n2)
        if sonuç == 31:
            print("BGUSUFGSDFOHUDFSGHJL")
        print(f"Hesap sonucu: {sonuç}")


    a = input("""
    Sonuçla başka işlem için 'b',
    Yeni rakalmlarla hesaplama yapmak için 'y',
    Hesaplamayı sonlandırmak için 's 'yazınız\n """)
    if a == "s":
        finish = True
        clear()
        print("Yine bekleriz.")
    
    elif a == "b":
        n1 = sonuç
        again = True
       
    else:
        again = False
        clear()
        print(logo)
        
    
        
        

        
            
        