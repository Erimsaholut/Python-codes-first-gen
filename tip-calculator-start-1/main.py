#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Kardeşler Lokantası Hesap Paylaştırıcısına hoşgeldiniz.")
toplam_hesap = float(input("Toplam Hesap Ne Kadar ?\n"))
yüzde_bahşiş = float(input("Yüzde Kaç Bahşiş Bırakmak İstersiniz ? (10, 15 , 20)\n"))
kişi_sayısı = int(input("Kaç Kişisiniz ? \n"))
bahşişli_yeni_hesap = (toplam_hesap/100)*(100+yüzde_bahşiş)
kisi_bası = round(bahşişli_yeni_hesap / kişi_sayısı,2)
print(f"Kişi başı hesap {kisi_bası}₺ tutuyor.")
if yüzde_bahşiş== 0 :
  print("ananın amına koyayım bahşiş bıraksana")
else:
  print("Teşekkür ederiz, Hayırlı Günler Dileriz.")