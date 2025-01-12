open_file = open("../Write/Contoh_write_text.txt","r")
read = open_file.read()
print("Value file Contoh_write_text.txt")
print(read)
# reset cursor
open_file.seek(0)

print("Ambil 1 baris di depan dari file Contoh_write_text.txt")
for line in open_file:
    if line.startswith("lokasi"): # gunanya untuk shoring search kata awal nya apa ? 
                print(line.strip()) # ini untuk mengambil 1 baris
                break
            
open_file.close()

