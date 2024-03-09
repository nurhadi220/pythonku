print("halooo")
a = 10
b = 3
c = a - b

print(c)
#aku ingin membuat algoritma selain perkalian,pembagian,penjumlahan dan pengurangan
hasil = a**b
print(a,"**",b,": ",hasil, "ini sebuah pemangkatan")

hasil = a%b
print(a,"%",b,": ",hasil, "ini sebuah modulus")

hasil = a//b
print(a,"//",b,": ",hasil, "ini sebuah float division") #hasil akhir pembagian

# di sini saya mau coba compali sejenis migration m(mode/model) di laravel, gunanya untuk mempercepat kinerja suatu program
# caranya dengan mengetiknya seperti ini (python -m py_compile tes.py) di terminal
# untuk cara menjalankan compile nya dengan menegtikan(__pycache__/(tab))

# cara mengubah tipe data di sini
r = 9
print("contoh:", r , "bertipe data", type(r))

ubah_ke_integer = str(r)
print("contoh:", ubah_ke_integer , "bertipe data", type(ubah_ke_integer))

ubah_ke_float = float(r)
print("contoh:", ubah_ke_float, "bertipe data", type(ubah_ke_float))

ubah_ke_bool = bool(r) #akan false jika nilai dari variabel 0
print("contoh:", ubah_ke_bool, "bertipe data", type(ubah_ke_bool))