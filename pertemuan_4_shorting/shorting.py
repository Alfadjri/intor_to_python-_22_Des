import random #pakage atau libary

def random_generate_angka(banyak_data):
    list_data = []
    for i in range(banyak_data):
        nilai_acak = random.randint(1,100)
        list_data.append(nilai_acak)
    return list_data

def short_bubble(data):
    n = len(data) #len digunakan untuk mengukur panjang data
    #logic
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j] > data[j+1]: # logic asc
                # tmp = data[j]
                # data[j] = data[j+1]
                # data[j+1] = tmp
                data[j],data[j+1] = data[j+1], data[j]

def short_select(data):
    n = len(data)
    #logic
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if data[j] < data[min_index]: #logic des
                min_index = j
        # tmp = data[i]
        # data[i] = data[min_index]
        # data[min_index] = tmp
        data[i],data[min_index]= data[min_index], data[i]
            

banyak_data = int(input("Banyak data yang akan di shorting : "))
list_data = random_generate_angka(banyak_data)
print("list data yang belum di urutkan : ")
print(list_data)
print("List data setelah di shorting")
# short_bubble(list_data)
short_select(list_data)
print(list_data)

