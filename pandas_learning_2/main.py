import numpy as np
import pandas as pd

dictData = {"İstanbul": [30, 29, np.nan], "Ankara": [20, np.nan, 31], "İzmir": [41, 39, 38]}
havaDurumuDF = pd.DataFrame(dictData)

print(havaDurumuDF)
print("\n")

print(havaDurumuDF.dropna())  # Dropna içerisnde not avalible olan satırları sildi (kalıcı için inplace)
print("\n")

print(havaDurumuDF.dropna(axis=0))  # içerisinde nan olmayan satırı getirdi
print(havaDurumuDF.dropna(axis=1))  # içerisinde nan olmayan sütunu getirdi
# hocam içerisinde 1 tane nan var diye bütün satır sütun silinir mi
# belirli bi sayıdan fazla varsa silmeyi yapıcaz yukarıda
print("\n")

newData = {"İstanbul": [30, 29, np.nan], "Ankara": [20, np.nan, 31], "İzmir": [41, 39, 38],
           "Trabzon": [23, np.nan, np.nan]}

newDF = pd.DataFrame(newData)
print(newDF)

print(newDF.dropna(axis=1, thresh=2))  # nan sayısı 2 ve üzeriyse onları atıyor
print("\n")
print(newDF.dropna())

print("\n")

print(newDF.fillna(-123))  # bu da boş yerleri istediğin şeyle dolduruyor

print("\n################\n")
maasSozlugu = {"Departman": ["Yazılım", "Yazılım", "Pazarlama", "Pazarlama", "Hukuk", "Hukuk"],
               "Calisan Ismi": ["Ahmet", "Mehmet", "Atil", "Burak", "Zeynep", "Fatma"],
               "Maas": [100, 150, 200, 300, 400, 500]
               }

maasDataFrame = pd.DataFrame(maasSozlugu)
maasDataFrame["Yas"] = np.random.randint(23, 60, 6)
print(maasDataFrame)

groupObject = maasDataFrame.groupby("Departman")
# Bu pandasın en destansı özelliği seçitiğin rowa göre gruplayıp birçok özellik sunuyor
print(groupObject.count())  # bu departmanına göre çalışan kişi sayısını veriyor

# print(groupObject.mean()) # bu da maaşlarının ortalamasını veriyor ama Feature warning atıyor

print(groupObject.max())  # bölümlere göre maks maaş alanlar

print(groupObject.min())  # bunlar da en az maaş alan garipler

print(groupObject.describe())  # bu da her şeyi veriyor.
# sonrasında yas sütunu ekledim ve anladığım kadarıyla int bulduğu her veriyi hesaplıyor destansı !

print("\n################\n")

sozluk1 = {"Isim": ["Ahmet", "Mehmet", "Zeynep", "Atıl"],
           "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
           "Kalori": [100, 200, 300, 400]
           }
dataFrame1 = pd.DataFrame(sozluk1, index=[0, 1, 2, 3])

sozluk2 = {"Isim": ["Osman", "Levent", "Atlas", "Fatma"],
           "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"],
           "Kalori": [200, 100, 50, 300]
           }
dataFrame2 = pd.DataFrame(sozluk2, index=[1, 2, 4, 5])

sozluk3 = {"Isim": ["Ayse", "Mahmut", "Duygu", "Nur"],
           "Spor": ["Koşu", "Yüzme", "Badminton", "Tenis"],
           "Kalori": [300, 400, 500, 250]
           }
dataFrame3 = pd.DataFrame(sozluk3, index=[1, 2, 5, 31])

print(pd.concat([dataFrame1, dataFrame2, dataFrame3]))

print("\n################\n")

mergeSozluk1 = {"Isim": ["Ahmet", "Mehmet", "Zeynep", "Atıl"],
                "Spor": ["Koşu", "Yüzme", "Koşu", "Basketbol"]
                }

mergeDataFrame1 = pd.DataFrame(mergeSozluk1)

mergeSozluk2 = {"Isim": ["Ahmet", "Mehmet", "Zeynep", "Atıl"],
                "Kalori": [100, 200, 150, 250]
                }

mergeDataFrame2 = pd.DataFrame(mergeSozluk2)
print(mergeDataFrame1, "\n\n", mergeDataFrame2)
mergedDataFrame = pd.merge(mergeDataFrame1, mergeDataFrame2, on=["Isim"])
print("\n\n", mergedDataFrame)
# concat arka arkaya eklerken mergede ortak columnu söyleyip baya baya birleştiriyoruz tabloları

maasSozlugu = {"Isım": ["Ali", "Ahmet", "Osman", "Aykut"], "Departman": ["Yazilim", "Satis", "Pazarlama", "Yazilim"]}
maasDataFrame2 = pd.DataFrame(maasSozlugu)
print("\n")

print(maasDataFrame2["Departman"].unique())  # sadece departman çeşitlerini getirdi

print(maasDataFrame2["Departman"].nunique())  # kaç çeşit departman var

print(maasDataFrame2["Departman"].value_counts())  # hangi departmandan kaçar tane insan var


def bruttenNete(maas):
    return maas * 0.66


print(maasDataFrame["Maas"].apply(bruttenNete))  # .apply ile kolayca foonksiyonları uygulayabiliriz

print("\n######\n")

yeniBirVeri = {"Karakter Sinifi": ["South Park", "South Park", "Simpson", "Simpson", "Simpson"],
               "Karakter Ismi": ["Cartman", "Kenny", "Homer", "Bart", "Bart"],
               "Karakter Yas": [9, 10, 50, 20, 10],
               }
characterDf = pd.DataFrame(yeniBirVeri)
print(characterDf.pivot_table(values="Karakter Yas", index=["Karakter Sinifi", "Karakter Ismi"]))
# bu da düzenlemek için ayrıca aynı değerlerin ortalamasını alıyor.
print(characterDf.pivot_table(values="Karakter Yas", index=["Karakter Sinifi", "Karakter Ismi"], aggfunc=np.sum))
# bunu eklersekte toplamını alıyor aynı olanların
