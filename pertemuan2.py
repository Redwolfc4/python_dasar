# ANGKA_KONSTANTA = 12

# print(ANGKA_KONSTANTA)

# ANGKA_KONSTANTA = 10
# print(ANGKA_KONSTANTA)

# nama_variable = 10
# print(nama_variable)

# variable1 = 12
# print(variable1)

# variable@ = 10
# print(variable@)

# variable-nama = 13
# print(variable-nama)

variable1 = 10*3
print(variable1)

# integer
jumlahSisiPersegiPanjang = 10
print(jumlahSisiPersegiPanjang)

# float
float_angka = 10.5
print(float_angka)

# boolean
boolean_true = True
print(boolean_true)

boolean_false = False
print(boolean_false)

# string
# inline string
string_kata = 'Aku belajar di Haltev'
print(string_kata)

# multiline String(docs)
string_multiline = """
ini adalah baris 1
ini adalah baris 2
ini adalah baris 3
"""

print(string_multiline)

# casting
angka_int_to_int = int(1)
angka_float_to_int = int(2.5)
angka_string_to_int = int("3")

print(angka_int_to_int, angka_float_to_int, angka_string_to_int)

# float
angka_string_float_to_float = float("3.5")
angka_int_to_float = float(3)
angka_string_int_to_float = float('3')

print(angka_string_float_to_float, angka_int_to_float, angka_string_int_to_float)

#string
angka_int_to_string = str(1)
angka_float_to_string = str(2.5)
print(angka_int_to_string,angka_float_to_string) #ini otomatis spasi dengan ,
print(angka_int_to_string+angka_float_to_string)
print(angka_int_to_string+" "+angka_float_to_string)
print(type(angka_int_to_string),type(angka_float_to_string))

# format string 
price_fruit = 50000
string_format = f"harga buah = {'Rp'} {price_fruit}" #cara1
print(string_format)
string_format = "harga buah = {} {}".format('Rp',price_fruit) #cara2
print(string_format)
string_format = f"harga buah = {'Rp'} {price_fruit:.2f}"#ubah jadi string float
print(string_format)

# escape character 
string_escape = 'Aku seorang developer "Python" di Haltev'#cara akalin string
print(string_escape)
string_escape = "Aku seorang developer \"Python\" di Haltev"#cara escape string
print(string_escape)

# operator aritmatika
a = 20
b = 6
print(a//b)#pembagian bulat
print(a%b)#pembagian sisa
print(a**b)# eksponent atau pangkat
print()

# operator pembanding
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print()

# Operator Logika
print((a>b) and (a==b))
print((a>b) or (a==b))
print(not ((a>b) or (a==b)))