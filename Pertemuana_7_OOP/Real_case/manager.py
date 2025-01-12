from employee import Employee

class Manager(Employee):
    def __init__(self,nama , umur , gaji , jumlah_tim):
        self._pekerjaan = "Product Manager"
        super().__init__(nama,umur,self._pekerjaan,gaji)
        self._jumlah_tim = jumlah_tim  # Ubah menjadi protected
    
    def get_detail(self):
        return f"Manger : {self._nama}, Age : {self.getUmur()},Job : {self._pekerjaan},Gaji : {self._gaji},Jumlah kariawan : {self._jumlah_tim}"
    
    def getPekerjaan(self):
        return f"{self._nama} dia bekejra sebagai manager tim sebesar {self._jumlah_tim} orang"