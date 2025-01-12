#while
#kita gak tau mau di ulang berapakali tapi kita tau kapan harus berhenti
#di akan di check terlebih dahulu
index = 200
print("==== while ====")
while(index <= 200):
    print(f"index value ke-{index} : Love you ")
    index += 1
    
# for
# kita tau kampan harus berhenti
print("==== for ====")
for i in range(0):
    print(f"index value ke-{i} : Love you ")
    

buahs = ["pisang","jamu","semangka","jeruk"]
print("ada makanan apa aja di sini")
for value in buahs:
    print(f"{value}")

# continue : melakuakan skip suatu nilai
# break : memaksa berhenti program looping
# contoh : 
# print angka dari 1 sampai 100  
# tampilkan angka yang ganjil saja 
# paksa berhenti di 40
index = 1
while( index <= 100) :
    if index % 2 != 0:
        print(f"Hasil setelah di modulus : {index}")
        index += 1
        continue # skip 1 putaran
    
    print(f"{index}")
    index += 1
    print(f"Hasil setelah di incerment : {index}")
    if (index == 40):
        break