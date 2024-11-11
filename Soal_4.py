# NAMA : BIMO ALVIANA SOPIAN
# NIM  : 2403010071
# KELAS: C
kalimat = input("Masukkan kalimat: ")

jumlah_vokal = 0

vokal = "aeiouAEIOU"

for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

print(f"Jumlah huruf vokal: {jumlah_vokal}")
