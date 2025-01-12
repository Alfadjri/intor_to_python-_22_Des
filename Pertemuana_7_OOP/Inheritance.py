class Ibu:
        panggilan = "ini punya ibu"
        # __sifat = "default"
        # method
        def memanggil(self):
            print("iya ,Ada apa ? ")
        
        def setSifat(self,sifat):
            self.__sifat = sifat
        
        def getSifat(self):
            return self.__sifat
    
class Anak(Ibu):
        def suruh(self):
            print("Nanti dulu deh lagi sibuk")
            
fadjri = Anak()
Ibu = Ibu()
Ibu.setSifat("Pemalu")

print("Sifat ibu ini gimana ?")
sifat = Ibu.getSifat()
print(sifat)

print("Sifat pajri ini gimana ?")
sifat = fadjri.getSifat()
print(sifat)


