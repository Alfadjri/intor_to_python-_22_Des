#int
#intenger adalah angaka bulat
x = 327678
print("ini contoh bilangan integer : {0}".format(x))
# float
f = 10.5
print("ini contoh bilangan float : {0}".format(f))
# kompleks
z = 2+3j
print("ini contoh bilangan kompleks : {0}".format(z))

#sqyence type
a = [1,2,3,4] # list : sifatntya tipe datanya harus sama dan tidak bisa di ubah
a = a + [3]
print("ini contoh bilangan list : {0}".format(a))
b = (3,4,5) # truplet : sifatnya gak bisa di ganti
print("ini contoh bilangan truplet : {0}".format(b))
c = range(0,5) # range 
print("ini contoh tipe data reange : {0}".format(c))

#type text
#strings
nama = "Alfadjri Dwi Fadhilah"
print("ini contoh tipe data string : {0}".format(nama))
#tipe data maping
profile = {"nama" : "Alfadjri Dwi Fadhilah","age" : 24}
print("ini contoh tipe data maping : {age} , {nama}".format(age = profile["age"],nama = profile["nama"]))

#set tipe
d = {1,2,3} # set
print("ini contoh tipe data set : {0}".format(d))
g = frozenset({4,"5",6,7}) #frozenset
print("ini contoh tipe data frozenset : {0}".format(g))

#bool
# bool ini nilainya hanya 2 true(1) dan false(2)
kondisi_badan = True

#binary type
i = 0b01000001
# desimal = int(i)
# char = chr(desimal)
# print(char)
print(chr(int(i)))
j = bytearray(a)
print(j)
k = memoryview(j)
print(k)


