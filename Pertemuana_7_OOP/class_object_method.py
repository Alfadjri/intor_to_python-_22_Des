class Hewan: #ini sebutanya class
    #property sifat dari objectnya
    nama_hewan = "default" #propery public masuknya pad object = nama_hewan
    _umur_hewan = 10 # propery private
    #metode
    #construktor
    def __init__(self,nama,jenis):
        self.nama_hewan = nama
        self.jenis_hewan = jenis
    # fungsi atau method
    def getMakan(self):
        print("Hewan sedang makan !!!")
        
# Cara panggil
kucing = Hewan("Tom","Kucing")
print(f"Nama hewan {kucing.nama_hewan}")
kucing.nama_hewan = "Kiti"
print(f"Nama hewan {kucing.nama_hewan}")
# cara panggil metode atau function
kucing.getMakan()
    