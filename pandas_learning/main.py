import numpy as np
import pandas as pd

# SERİLER

myDict = {"Erim": 50, "Zeynep": 30, "Mohammad": 99}
myDict = pd.Series(myDict)
print(myDict)
print(type(myDict))
print("\n")

myNameList = ["Erim", "Zeynep", "Mohammad"]
myAgeList = [50, 30, 99]
print(pd.Series(data=myAgeList, index=myNameList))
print("\n")

numpyList = np.array([50, 40, 30])
numpyList = pd.Series(numpyList)
print(numpyList)
print("\n")
# Burada şair demiş ki dict list ve array fark etmeden pd.Series oluşturabilirsin

a = pd.Series([93, 36, 68], ["Ankara", "Bursa", "Cizre"])
b = pd.Series([6, 63, 31], ["Ankara", "Bursa", "Cizre"])
print(a)
print(a["Ankara"])
print("\n")

print(a + b)

# DATAFRAME
myMatrix = np.random.randn(4, 3)

myMatrix = np.random.randint(-100, 100, (4, 3))

print(myMatrix)

myDataFrame = pd.DataFrame(myMatrix)
print(myDataFrame)
print("##")
print(myDataFrame[0])
print(type(myDataFrame[0]))  # bunun series çıkması dataframein serileri yan yana koyması anlamına geliyor
print(type(myDataFrame))

myNewDataFrame = pd.DataFrame(myMatrix, index=["Bir", "Ni", "Three", "Vier"], columns=["Akp", "Chp", "Mhp"])
# index ve columnları kendimiz belirleyebiliriz
print(myNewDataFrame)
print(type(myNewDataFrame))
print("##")
print(myNewDataFrame["Akp"])
print(myNewDataFrame[["Chp", "Mhp"]])  # Böyle karşılaştırmalı aramalar da yapılabilir
print("##")
print(myNewDataFrame.loc["Bir"])  # Satırla arama yapmak için bir de loc ekliyoruz
print(myNewDataFrame.iloc[0])  # Yine aynı satırla ama yapmak için ama buna index giriyoruz.

print("##")

myNewDataFrame["hdp"] = np.random.randint(-100, -10, 4)
print(myNewDataFrame)
myNewDataFrame["IQ seviyesi"] = np.random.randint(60, 140, 4)
print(f"{myNewDataFrame}\n\n")

print(myNewDataFrame.drop(["IQ seviyesi"], axis=1))  # bunlar column ve row silmek için ama sadece
print(myNewDataFrame.drop(["Vier"], axis=0))  # print yaptığında gözüküyor print(myNew...)yapınca aynı
print(myNewDataFrame.drop(["IQ seviyesi"], axis=1, inplace=True))  # bu kalıcı yapıyor
print(myNewDataFrame)

print("\n###\n")

print(myNewDataFrame.loc["Bir"]["Akp"])
print(myNewDataFrame.loc["Ni", "Chp"])  # belirli bir hücreyi almak için

print("\n###\n")
booleanFrame = myNewDataFrame < 0
print(booleanFrame)
print(myNewDataFrame[booleanFrame])  # sıfırdan büyük değerleri verdi burası da
print("\n")
print(myNewDataFrame["Chp"] > 0)
print(myNewDataFrame[myNewDataFrame["Chp"] > 0])  # bu şekilde chpnin 0 dan büyük olduğu yerleri yazdırdık

print("\n##########\n")

print(myNewDataFrame)
print(myNewDataFrame.reset_index())  # bu da index ekliyor ama kalıcı olması için inplace=True lazım
print("\n")

myNewIndexList = ["İstanbul", "İzmir", "Manisa", "Şırnak"]
myNewDataFrame["Yeni index"] = myNewIndexList
print(myNewDataFrame)

print(myNewDataFrame.set_index("Yeni index", inplace=True))
print(myNewDataFrame)

print("\n##########\n")

firstIndex = ["Manisa", "Manisa", "Manisa", "İzmir", "İzmir", "İzmir"]
secondIndex = ["Akhisar", "Turgutlu", "Şehzadeler", "Bornova", "Aliaga", "Karsiyaka"]
mergedIndex = list(zip(firstIndex, secondIndex))
mergedIndex = pd.MultiIndex.from_tuples(mergedIndex)
myDataList = [[200.000, "A+"], [170.000, "B-"], [250.000, "D"], [400.000, "A"], [300.000, "B"], [500.000, "A-"]]
myDataList = np.array(myDataList)
myCityDataframe = pd.DataFrame(myDataList, index=mergedIndex, columns=["Population", "My Score"])
print(myCityDataframe)
print("\n")
print(myCityDataframe.loc["Manisa"])
print(myCityDataframe.loc["İzmir"])
print("\n")
print(myCityDataframe.loc["İzmir"].loc["Bornova"])
print("\n")
myCityDataframe.index.names = ["City", "District"]
print(myCityDataframe)
