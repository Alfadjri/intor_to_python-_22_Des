from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, nama, umur):
        self._nama = nama  # Ubah menjadi protected dengan satu garis bawah
        self._age = umur   # Ubah menjadi protected dengan satu garis bawah
    
    @abstractmethod
    def get_detail(self):
        pass
    
    def getUmur(self):
        return self._age
    
    def setUmur(self, umur):
        if umur > 0:
            self._age = umur
        else:
            raise ValueError("Umur harus bernilai positif")
