siswa = {
    "kelas" : 12,
    "jurusan" : [
        "ipa","ips", ["Indonesia","inggris","","","",""]
    ],
    "nama_ketua" : "udin",
    "kosong" : "",
}
# cara membaca semua
print(f"Data metah : {siswa}")
# cara memanggil spesifik
print(f"Kelas :{siswa["kelas"]}")
print(f"jurusan: {siswa["jurusan"][2][3]}")
# menamabahkan data ini pastikan tidak ada key nya
siswa["nilai"] = 10
print(f"Data metah : {siswa}")
siswa["nilai"] = 30 # update pastikan key nya ada dalam data 
print(f"Data metah : {siswa}")
# hapus
del siswa["nilai"]
print(f"Data metah : {siswa}")