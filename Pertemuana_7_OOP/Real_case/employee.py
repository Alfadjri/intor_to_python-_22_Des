from person import Person

class Employee(Person):
    def __init__(self, nama, umur, pekerjaan, gaji):
        super().__init__(nama, umur)
        self._pekerjaan = pekerjaan
        self._gaji = gaji
        
    def get_detail(self):
        return f"Employee: {self._nama}, Age: {self._age}, Job: {self._pekerjaan}, Gaji: {self._gaji}"
    
    def getPekerjaan(self):
        return f"{self._nama} bekerja sebagai {self._pekerjaan}"
