def coba(A):
    for i in range (len (A)):
        A[i]=A[i]*len(A)
    return sum(A)

##bila mengikuti instruksi panjang
##menghitung number of data yang ada dalam suatu list 
##kemudian jumlah data di list tersebut, dikalikan dengan masing-masing data di dalam list
##angka-angka tersebut kita jumlah

def hitung_data_di_list(data_dalam_list):
    n = len(data_dalam_list)
    return n

def kalikan_angka_di_list(data_dalam_list,jumlah_data_di_list):
    list_new=[]
    for i in range (jumlah_data_di_list):
        list_new.append(jumlah_data_di_list * data_dalam_list[i])
    return list_new

def jumlah_data_di_list(list_yang_baru):
    hasil_akhir = sum(list_yang_baru)
    return hasil_akhir

if __name__ == '__main__':
    import sys
    a = int(input("Enter your number:"))
    angka = a*10
    print ("Your number after multiply by 10 is:" + angka)