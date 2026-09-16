def nilai_akhir(tugas, uts, uas):
    """
    Menghitung nilai akhir dengan bobot:
    - Tugas = 20%
    - UTS = 30%
    - UAS = 50%
    """
    return (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)

def rata_rata(daftar_nilai):
    """Menghitung rata-rata dari list nilai"""
    return sum(daftar_nilai) / len(daftar_nilai)
