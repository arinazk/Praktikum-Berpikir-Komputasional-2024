sudah_isian = int(input("Masukkan banyak soal isian singkat yang sudah diselesaikan : "))
sudah_esai = int(input("Masukkan banyak soal esai yang sudah diselesaikan : "))
waktu_belum_isian = (14 - sudah_isian) * 10
waktu_belum_esai = (2 - sudah_esai) * 20
total_waktu = waktu_belum_isian + waktu_belum_esai

if total_waktu < 60:
    print("Tuan Riz akan berhasil mengerjakan semua soal")
else: 
    print("Tuan Riz tidak akan berhasil mengerjakan semua soal")