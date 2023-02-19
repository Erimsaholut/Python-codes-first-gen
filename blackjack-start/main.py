import random
from art import logo
from replit import clear

bitir = False

    

def yirmibir():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(logo)
    user_cards = []
    computer_cards = []
    def toplapc():
        return sum(computer_cards)
    def toplasen():
        return sum(user_cards)
    selection_finish = False
    passed_21_or_user = False
    #Oyuncu için kart seçtik
    user_cards += random.choices(cards, k=1)
    sonraki_kart = random.choices(cards, k=1)
    if sonraki_kart[0] + user_cards[0] == 22:   ## 2 kere 11 çekmesi durumunda 11 i 1 olarak kullanma
        user_cards.append(sonraki_kart[0] - 10)
    else:
        user_cards += sonraki_kart
    print(f"Senin kartların:{user_cards},Toplam skorun {[toplasen()]}")
    #en başında 21 çekersek
    if toplasen() == 21:
        print("Tek attın aslanım😎😎😎😎😎")
        selection_finish = True
        passed_21_or_user = True

    #bilgisayar için kart seçiyoruz
    computer_cards += random.choices(cards, k=1)
    print(f"Bilgisayarın ilk kartı: {computer_cards} ")

    #yeni kart çekme fonskiyonunu tanımlayalım

    def yeni_kart():
        yenikart = random.choices(cards, k=1)
        user_cards.extend(yenikart)
        print(f"Senin Kartların:{user_cards},Toplam skor: {[toplasen()]}")

    #####kart çekme işlemleri

    while not selection_finish:
        ask = input("Yeni kart için 'y' yazınız, pas geçmek için 'n' yazınız: ")
        if ask == "y":
            yeni_kart()
        elif ask == "n":
            selection_finish = True
        else:
            print("Adam gibi yaz boğazını keserim senin")
        if toplasen() > 21:                          ##oyuncudan dolayı oluşan kaybetme durumları 
            selection_finish = True
            passed_21_or_user = True
            print("Toplam sayı 21i geçtİ. Kaybettin 😭")
        if toplasen() == 21:
            selection_finish = True
            passed_21_or_user = True
            print("Kazandın 🥳🤩😎")

    #bilgisayar kartları

    while not passed_21_or_user and selection_finish:
        if toplasen() > toplapc():
            if toplapc() < 21:
                computer_cards += random.choices(cards, k=1)
        elif toplapc() == 21:  ##mesela 18 18 berabere kalmasınlar diye kart çekiyor 
            print(f"Senin Kartların:{user_cards},Toplam skor: {[toplasen()]}")
            print(f"Bilgisayarın son eli:{computer_cards}, son skor: {[toplapc()]}")
            passed_21_or_user = True
        elif toplasen() == toplapc() and toplapc()<21 :
            computer_cards += random.choices(cards, k=1)
            
        else:  
            print(f"Bilgisayarın son eli: {computer_cards}, son skor: {toplapc()}")
            passed_21_or_user = True

    # kazananı belirle
    if toplapc() > 21:
        print(f"Senin Kartların:{user_cards},Toplam skor: {[toplasen()]}")
        print("Kazandın 🥳🤩😎")
    elif toplapc() > toplasen() :
        print("Kaybettin adamımım 😫")
    if toplapc() == toplasen():
        print("Berabere")


while not bitir: 
    yirmibir()
    bitsin_mi = input("Yeni oyun için 'y',oyunu bitirmek için 'n' yazınız.")
    if bitsin_mi == "n":
        bitir = True
    else:
        clear()
