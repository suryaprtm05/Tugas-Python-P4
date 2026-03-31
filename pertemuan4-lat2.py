# Input jumlah hari
x = int(input("Masukkan jumlah hari proyek: "))

# Proses konversi
tahun = x // 365
sisa_hari = x % 365

bulan = sisa_hari // 30
hari = sisa_hari % 30

# Output hasil
print("Lama proyek:")
print("Tahun :", tahun, "Tahun")
print("Bulan :", bulan, "Bulan")
print("Hari  :", hari, "Hari")