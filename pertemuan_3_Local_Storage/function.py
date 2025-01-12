#function
#format_dasar
#function(syarat_atau_paramter)
#format
#def namaFunction (syarat):
#  apa yang mau di lakukan'
#cara memanggil
#namaFunction(syarat)

def printNama (nama):
    return f"Hello , {nama}"
# Cara manggil
v1 = printNama("Alfadjri")
v2 = printNama("Joko")
v3 = printNama("Budi")

print(v1)
print(v2)
print(v3)


def printNama_2(nama):
    print(f"Hello, {nama}")
    print(f"Testing, {nama}")

printNama_2("Alfadjri")
printNama_2("joko")

def tambah(a,b):
    return a + b

hasil = tambah(10,5)
print(f"Hasil kalulasi antara 10 + 5 = {hasil}")