class Mobil:
        def hidupkan_mesin(self):
            return "Mobil menggunakn bensin menyala"
        
class Mobil_Listrik(Mobil):
        def hidupkan_mesin(self):
            return "Mobil listirk low Batter"


def start(Mobil):
    print(Mobil.hidupkan_mesin())
    
toyota = Mobil_Listrik()
start(toyota)