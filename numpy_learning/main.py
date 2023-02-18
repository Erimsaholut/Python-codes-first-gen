import numpy as np

# NUMPY ARRAY

my_list = [20, 30, 40]
print(np.array(my_list))
print(type(np.array(my_list)))

matrix_list = [[10, 20, 30], [45, 55, 65], [77, 88, 99]]

print(np.array(matrix_list))  # listeyi matrix olarak yazdı konsola

# NUMPY ARRANGE
print("\n#####################\n")

print(np.arange(0, 10))
print(np.arange(0, 20, 3))  # sırali liste oluşturuyor, istersen atlamalı

# NUMPY ZEROS, ONES
print("\n#####################\n")

print(np.zeros(5))
print(np.zeros((3, 3)))
print(np.ones((4, 4)))  # sıfır veyahut birlerden, liste veyahut matrix

# LİNSPACE

print(np.linspace(0, 20, 5))  # 0 dan 10 a kadar 5 eleman olacak şekilde eşit mesafelerle ayır

# EYE
print("\n#####################\n")

print(np.eye(5))  # çaprazlı matrix

# RANDOM

print(np.random.randn(6))  # aralıksız rastgele değer döndürüyor
print(np.random.randn(3, 3))  # randomke matrixke

my_array = np.random.randint(1, 100, 40)  # bu da int döndürüyor

# NUMPY ARRAY METHODS

print(my_array.reshape(5, 8))  # listeyi istenen şekilde düzenledi
print(f"maks value: {my_array.max()}")
print(f"min value: {my_array.min()}")
print(f"maks_index: {my_array.argmax()}")  # bu maksimum ve minimumun kaçıncı indexte olduğunu söylüyor
print(f"min_index : {my_array.argmin()}")

# NUMPY OPERATIONS
print("\n#####################\n")

my_list = np.arange(0, 23)
my_list[3:8] = -5  # aralıktaki herkes -5 oldu
print(my_list)

my_list2 = my_list[7:14]  # ilk diziden bir aralık aldık ve garip bir şekilde bağlantılı kalıyorlar
print(my_list2)

my_list2[:] = 23  # bütün dizi 23 oldu [:] böyle yapınca herkesi çağırıyor.
print(my_list2)
print(my_list)  # yeni bir liste yaratmış olsakta ikinciyi değiştirince bu da değişti

# bunun olmamasını istiyorsak
print("---")
my_list3 = my_list.copy()
my_list3[5:15] = 515
print(my_list3)
print(my_list)  # kopyaladığımız için ilk diziye etki etmedi

# MATRİX COMANDS
print("\n#####################\n")
ornek_matrix = np.array(matrix_list)
print(ornek_matrix)
print(f"\n{ornek_matrix[2][0]}")
print(ornek_matrix[2, 0])  # bu ikisi aynı şey
print(f"\n{ornek_matrix[0:, 2]}")  # bu şekilde sütun çağırıyor [hangi sıradan başlasın:, hangi sütunu alsın]
print(f"\n{ornek_matrix[0:, 2:]}\n")  # bu da böyle

print(f"{ornek_matrix}\n")
print(ornek_matrix[[0, 1]])  # [[]] bu şekilde birden fazla satırı çağırabilirsin

# OPERATİONS
print("\n#####################\n")

my_array = np.random.randint(1, 100, 24)
print(my_array)
print(my_array > 26)  # 26 dan büyük elemanları döndürüyor true false olarak
print(my_array[my_array > 26])  # bu şekilde 26 dan büyük elemanları yazdı

print("\n")
last_array = np.arange(0, 20)
print(last_array)
print(last_array + last_array)
print(last_array - last_array)
# print(last_array / last_array) sıfır/sıfırda hata çıkarıyor bu
print(np.sqrt(last_array))
