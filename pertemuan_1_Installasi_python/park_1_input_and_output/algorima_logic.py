# kasus : kita koreksi nilai raport
# if
# if (kondisi) :
#  apa yang di lakukan kalau kondisinya terpenuhi
nilai_raport = 50
print("=========if=======")
if (nilai_raport > 80):
    print("Selamat kamu lulus dalam ujian kali ini")
#if else
nilai_raport = 90
print("=========if-else=======")
if (nilai_raport > 80):
    print("Selamat kamu lulus dalam ujian kali ini")
else :
    print("Mohon maaf kamu tidak lulus pada ujian kali ini !")
# teknik singkat
# tenary 
nilai_raport = 90
nilai_raport = "A" if nilai_raport >= 60 else "C"
print(f"Nilai raport : {nilai_raport}")

print("=========if-elif-else=======")
nilai_raport = 60
if (nilai_raport > 80):
    print("A") # perintah yang mau di lakukan dengan sayarat yang di sebutkan
elif(nilai_raport < 80 and nilai_raport > 80):
    print("B")
elif(nilai_raport < 70):
    print("C")
else :
    print("D")
    
#switch case 
#match case
print("===============================")
print("Selamat datang di aplikasi saya")
print("===============================")
print("1. Start")
print("2. Exit")
select = input("Selection => ")
match select :
    case "1":
        print("Start Game")
    case "2":
        print("Game Over")
    case "99":
        print("Selamat menu rahasia")
    case _ :
        print("Input in valid")