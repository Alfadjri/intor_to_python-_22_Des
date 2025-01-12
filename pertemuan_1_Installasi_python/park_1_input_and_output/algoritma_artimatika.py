x = 7
y = 3

# penjumlahan (+)
hasil = x + y
# print("Hasil penjumlahan dari {x} + {y} = {hasil}".format(x = x , y = y , hasil = hasil))
#cara singkat
print(f"Hasil penjumlahan dari {x} + {y} = {hasil}")
#pengurangan (-)
hasil = x - y
print(f"Hasil kurang dari {x} - {y} = {hasil}")
#perkalian(*)
hasil = x * y
print(f"Hasil kali dari {x} * {y} = {hasil}")
#pembagian(/)
hasil = x / y 
hasil = int(x/y) #tekinik casting atau conversi dari float ke integer
print(f"Hasil pembagian dari {x} / {y} = {hasil}")
#modulus
hasil = x % y
#logic
# logic  hasil = 7 / 3 = 7 - 6 = 1 (modulus = 1)
print(f"Hasil modulus dari {x} % {y} = {hasil}")
#pangkat
hasil = x ** y
print(f"Hasil pangkat dari {x} ** {y} = {hasil}")

# incdement
hasil = hasil + 1
print(f"nilai dari hasil : {hasil}")
hasil += 1
print(f"nilai dari hasil : {hasil}")
# decerment
hasil -= 1
print(f"nilai dari hasil : {hasil}")