min = int(input("Minimum Sayi giriniz: "))
while min<3:
	print("Lütfen ikiden büyük bir sayı girip tekrar deneyiniz !")
	min = int(input("Minimum Sayi giriniz: "))

maks = int(input("Maksimum sayı giriniz: "))
artis = int(input("Kacarli artacagini giriniz: "))

for i in range(min,maks,artis):
	print(i)
