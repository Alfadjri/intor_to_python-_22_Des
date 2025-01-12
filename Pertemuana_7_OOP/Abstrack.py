from abc import ABC 

class kendaraan(ABC):
    def menyalakan_mesin(self):
        pass
    
class Mobil(kendaraan):
        def menyalakan_mesin(self):
            return "Start"
class Mobil_listrik(kendaraan):
        def menyalakan_mesin(self):
            return "Engine Start"

Mobil_listrik = Mobil_listrik()
print(f"Suara waktu menyalakan : {Mobil_listrik.menyalakan_mesin()}")