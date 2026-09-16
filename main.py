import hitung
from laporan import cetak_laporan
from predikat import get_predikat

# Data mahasiswa (bisa juga pakai input)
nama = "Siti"
tugas = 85
uts = 78
uas = 90

akhir = hitung.nilai_akhir(tugas, uts, uas)
huruf_mutu = get_predikat(akhir)
cetak_laporan(nama, tugas, uts, uas, akhir, huruf_mutu)

# Contoh pakai fungsi rata-rata
daftar = [80, 85, 90, 75]
print("\nRata-rata kelas:", hitung.rata_rata(daftar))
