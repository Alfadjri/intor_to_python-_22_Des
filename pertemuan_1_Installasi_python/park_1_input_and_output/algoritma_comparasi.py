a = 10
b = 10
#besar dari (>)
hasil = ( a > b )
print(f"apakah {a} itu lebih besar dari (>) {b} : {hasil}")
#besar dari sama dengan (>=)
hasil = ( a >= b )
print(f"apakah {a} itu lebih besar dari sama dengan (>=) {b} : {hasil}")
#kecil dari (<)
hasil = ( a < b )
print(f"apakah {a} itu lebih kecil dari (<) {b} : {hasil}")
#kecli dari sama dengan (<=)
hasil = ( a <= b )
print(f"apakah {a} itu lebih kecil dari sama dengan (<=) {b} : {hasil}")
# equels persamaan (==)
a = 2
b = 2
hasil = (a == b)
print(f"apakah nilai {a} sama dengan (==) {b} : {hasil}")

# and ( && )
# and table 
# | && | 1 | 0 |
# | 1  | 1 | 0 |
# | 0  | 0 | 0 |
a = 10
b = 5
hasil = ( a < b and b == 5 )
print(f" hasil dari {hasil}")
# or ( || )
# or table 
# | || | 1 | 0 |
# | 1  | 1 | 1 |
# | 0  | 1 | 0 |
hasil = ( a < b or b == 5 )
print(f" hasil dari {hasil}")

# not (!) semua nilai di balik 
kondisi = False
hasil = (hasil != False) # apakah variabel kondisi tidak sama dengan True
print(f" hasil dari not (!) {hasil}")