from employee import Employee
from manager import Manager

def main():
        list_kariasan = [
            {
                "nama" : "Tika",
                "Umur" : 20,
                "Pekerjaan" : "Software Developer",
                "gaji" : 5000000,
                "total_kariawan" : None
            },
            {
                "nama" : "Bob",
                "Umur" : 40,
                "Pekerjaan" : None,
                "gaji" : 7000000,
                "total_kariawan" : 10
            },
            {
                "nama" : "Sister",
                "Umur" : 40,
                "Pekerjaan" : "Ui UX",
                "gaji" : 7000000,
                "total_kariawan" : None
            },
        ]
        for kariwan in list_kariasan:
            if(kariwan["total_kariawan"] != None):
                employee = Manager(kariwan["nama"] , kariwan["Umur"],kariwan["gaji"],kariwan["total_kariawan"])
            else:   
                employee = Employee(kariwan["nama"] , kariwan["Umur"] , kariwan["Pekerjaan"],kariwan["gaji"])
                
            print(employee.get_detail())
            print(employee.getPekerjaan())

if __name__ == "__main__":
    main()