from art import logo
# HINT: You can call clear() to clear the output in the console.
teklifler= {}
should_end = False


def bidle_bizi_ustam():
    print(logo)
    isim = input("İsminiz nedir ?")
    para = input ("Teklifiniz nedir ?")
    teklifler[isim] = para
    print(teklifler)
    clear()


while not should_end:
    bidle_bizi_ustam()
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    clear()
    if restart == "no":
        should_end = True       
ilkteklif = list(teklifler.values())[0]
for i in teklifler:
    if int(teklifler[i]) > int(ilkteklif):
        ilkteklif = teklifler[i]
        winner = i 

print(f"Kazanan {ilkteklif}₺ teklifi ile {winner}\n Kendisini tebrik ederiz.") 



a
a
a
a

