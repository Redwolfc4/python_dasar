# percobaan try and except
try:
    x = 10
    print(x)
except:
    print('terjadi error')
    
print('='*5)

# error case tipe data
try:
    x1 = '10'
    x2 = float(x1)
    xtotal = x1 + x2
    print(xtotal)
except:
    print('tipe data float tidak bisa dtambah dengan string')

print('='*5)

#  case dengan nama errornya
# try:
#     x1 = input('masukkan string angka : ')
#     x2 = int(x1)
#     xtotal = x1 - x2
#     print(xtotal)
# except ValueError:
#     print('nilainya bukan angka')
# except TypeError:
#     print('string tidak bisa logika dengan angka')


# tangkap zero divisiobnnya denga try except
# atur print error zero divisionnya dengan mesaage "tidak bisa dibagi nol"
# print(2/0)


# case paksa error
try:
    angka1 = int(input('Masukkan angka pertama : '))
    angka2 = int(input('Masukkan angka kedua : '))
    
    if (angka1 == angka2):
        raise Exception('angkanya sama gan')
    
    print(angka1/angka2)
except Exception as e:
    print(e)
