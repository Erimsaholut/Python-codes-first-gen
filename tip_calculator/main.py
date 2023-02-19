#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Kardeşler Lokantasına Hoş Geldiniz")
Para = float(input("Hesap ne kadar geldi ? "))
tip = float(input("Yüzde kaç bahşiş bırakmak isiyorsunuz ? %"))
tipi = Para/100*(100+tip)
insan = float(input("Kaç kişisiniz? "))
hesaps = tipi/insan
son = round(hesaps,2)
son = "{:.2f}".format(hesaps)
print(f"Kişi başı {son} TL ödeyin bakim")
print("Afiyet olsun \nYine bekleriz. \nKardeşler Lokanta© lti. sti Bütün hakları saklıdır. ")