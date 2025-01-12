# misal 
# makanan
# data
# id (sifatnya nomer unik yang mewakili data)
# value
# qty 
# create_at
# update_at
makanan = ["nasi","ikan","ayam","sayur","buah"]
# cara membaca
print(f"isi data list : {makanan}")
# membaca nilai spesifik
# namaVariabel[posisiData atau IndexData] ini di mulai dari 0
print(f"Lauk yang ada di piring saat ini : {makanan[1]}")
# update
# namaVariable[posisiData] = value terbaru
makanan[1] = "daging"
print(f"Lauk yang ada di piring saat ini setelah di update : {makanan[1]}")

makanan.append("nasi")
print(f"isi data list setelah update : {makanan}")

makanan.remove("nasi")
print(f"isi data list setelah update : {makanan}")

# menggabungkan 2 list
buah = ["semangka","pisang"]
makanan_baru = makanan + buah
print(f"isi data list setelah update : {makanan_baru}")