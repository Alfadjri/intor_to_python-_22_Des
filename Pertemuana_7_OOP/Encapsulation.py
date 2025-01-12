class Hewan:
        # set paramater itu bisanya di sebut inisilaisasi
        _nama = "default"
        _umur = "default"
        _jenis = "default"
        def __init__(self,name,age,type_hewan):
            self._nama = name
            self._umur = age
            self._jenis = type_hewan
        
        # seter and geter
        # get  untuk mengambil nilai
        def getName(self):
            return self._nama + " Testing"
        # set itu untuk merubah nilai
        def setName(self,name):
            self._nama = name


kucing = Hewan("Tom",2,"Kucing")
print(f"Nama hewan {kucing.getName()}")
kucing.setName("kiti")
print(f"Nama hewan {kucing.getName()}")