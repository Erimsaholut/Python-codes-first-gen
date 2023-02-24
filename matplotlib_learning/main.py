import numpy as np
import matplotlib.pyplot as plt

ageList = [10, 20, 30, 40, 50, 55, 57, 99, 99]
weightList = [30, 50, 33, 32, 55, 77, 99, 21, 29]
numpyAgeList = np.array(ageList)
numpyWeightList = np.array(weightList)
numpyArray = np.linspace(10, 100, 13)


def plt1():
    plt.plot(numpyAgeList, numpyWeightList, "black")  # değerleri verdik ve rengini green yaptık.
    plt.xlabel("Age")
    plt.ylabel("Weight")  # bunlarla labellara isim verebiliyoruz
    plt.title("Graph of comparison weight by age")  # tabloya title
    plt.show()


def plt2():
    plt.plot(numpyArray, numpyArray ** 4, "b*-")  ## bu da böyle konveks bi grafik
    # "g--" yaparsak kesikli "g*-" yaparsak noktalı grafik oluşturuyor
    plt.show()


def plt3():
    plt.subplot(1, 2, 1)  # 1 sıra olacak, 2 grafik olacak, 1.yi anlatıyorum
    plt.plot(numpyArray, numpyArray ** 3, "r--")
    plt.title("first")

    plt.subplot(1, 2, 2)  # 1 sıra 2. kolon 2.yi anlatıyorum
    plt.plot(numpyArray, numpyArray ** 11, "Black")
    plt.title("notFirst")  # ayrı ayrı başlık vermekte var

    plt.show()


def plt4():
    myFigure = plt.figure()
    figureAxes = myFigure.add_axes([0.4, 0.4, 0.6, 0.6])  # grafiğin boyutlarını belirleyebiliyoruz ama biraz garip
    # width, height
    figureAxes.plot(numpyArray, numpyArray ** 5, "Black")
    figureAxes.set_xlabel("X label data")
    figureAxes.set_ylabel("Y label data")
    figureAxes.set_title("Graph Title")
    plt.show()


def plt5():
    myFigure = plt.figure()

    axis1 = myFigure.add_axes([0.1, 0.1, 0.7, 0.7])
    axis2 = myFigure.add_axes([0.2, 0.4, 0.3, 0.3])

    axis1.plot(numpyArray, numpyArray ** 5, "r--")
    axis1.set_xlabel("X label data")
    axis1.set_ylabel("Y label data")
    axis1.set_title("Graph 1 Title")

    axis2.plot(numpyArray ** 5, numpyArray, "b--")
    axis2.set_xlabel("X label data")
    axis2.set_ylabel("Y label data")
    axis2.set_title("Graph 2 Title")

    plt.show()  ## grafik içinde grafik çıktı


def plt6():
    (myFigure, myAxis) = plt.subplots(nrows=1, ncols=2)
    print(type(myAxis))

    for axis in myAxis:
        axis.plot(numpyArray, numpyArray ** 3, "r")
        axis.set_xlabel("X axis")

    plt.tight_layout()  # bu çok yakın duran grafiklerin arasını açıyor
    plt.show()


def plt7():
    newFigure = plt.figure(dpi=100)
    # figsize = (9, 9) ile grafiğin boyutlarını belirleyebilirsin ama boş bırakırsan otomatik
    # dpi = dot per inch, çözünürlüğü arttırıyor

    newAxis = newFigure.add_axes([0.1, 0.1, 0.9, 0.9])

    newAxis.plot(numpyArray, numpyArray ** 3, label="NumpyArray ** 3")
    newAxis.plot(numpyArray, numpyArray ** 3.5, label="NumpyArray ** 3.5")
    newAxis.legend(loc=1)
    # loc 1 2 3 4 5 yazıp farklı yerlerde çıkarabiliyorsun tabloyu

    # newFigure.savefig("myFigure.png",dpi=200) # dosya olarak kaydetmek için
    plt.show()


def plt8():
    (myFigure, myAxis) = plt.subplots()
    myAxis.plot(numpyArray, numpyArray * 3, "red", linewidth=3.0)  # linewidth kalınlığı ayarlıyor
    myAxis.plot(numpyArray * 2, numpyArray, color="#6B98B9")  # kendimiz renk ekliyoruz
    myAxis.plot(numpyArray * 3, numpyArray, color="#EB455F", alpha=0.1)  # saydamlığını azalttı default =1
    myAxis.plot(numpyArray * 4, numpyArray, color="#F99417", linestyle=":")  # çizgi stili "--" , ":" , "-." gibi
    myAxis.plot(numpyArray * 5, numpyArray, color="#5D3891", marker="o", markerfacecolor="red")
    # bu da tam verilerin olduğu yeri işaretliyor "o","*","+" gibi

    plt.show()


def plt9():
    plt.scatter(numpyArray, numpyArray ** 2)  # dağıtılmış çizgiler
    plt.show()


def plt10():
    numpyArray = np.linspace(0, 20, 15)  # histogram grafiği ama kötü duruyor
    plt.hist(numpyArray)
    plt.show()


def plt11():
    plt.boxplot(numpyArray ** 2)  # lan bu ne
    plt.show()

# https://matplotlib.org/stable/tutorials/index.html#tutorials
# for more and more
