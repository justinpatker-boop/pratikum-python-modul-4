import predikat


def cetak_laporan(nama, tugas, uts, uas, akhir, predikat):
    print("==== LAPORAN NILAI ====")
    print(f"Nama Mahasiswa  : {nama} ")
    print(f"Tugas           : {tugas} ")
    print(f"UTS             : {uts} ")
    print(f"UAS             : {uas} ")
    print(f"Nilai Akhir     : {akhir:.2f} ")
    print(f"Predikat : {predikat}")
    print("=======================")