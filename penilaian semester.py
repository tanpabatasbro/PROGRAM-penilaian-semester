print(f"{'PROGRAM PENILAIAN SEMESTER':^40}")
print(f"{'='*40 :^40}")

nama = input("Masukkan Nama :")
nim = input("Masukkan Nim :")
kelas = input("Masukkan Kelas  :")
matkul = input("Masukkan Mata Kuliah :")
absen = float(input("Masukkan Nilai Absen :"))
tugas = float(input("Masukkan Nilai Tugas :"))
kuiss = float(input("Masukkan Nilai Kuiss :"))
uts = float(input("Masukkan Nilai UTS :"))
uas = float(input("Masukkkan Nilai UAS :"))


nilai_absen = int(absen * 15/100)
nilai_tugas = int(tugas * 20/100)
nilai_kuiss = int(kuiss * 10/100)
nilai_uts = int(uts * 25/100)
nilai_uas = int(uas * 30/100)

nilai_akhir = nilai_absen + nilai_tugas + nilai_kuiss + nilai_uts + nilai_uas

print(f"{'='*40 :^40}")
print(f"{'NILAI FINAL':^40}")
print(f"{'='*40 :^40}")

print(f"Nama\t\t : {nama}")
print(f"Nim\t\t : {nim}")
print(f"Kelas\t\t : {kelas}")
print(f"Mata Kuliah\t : {matkul}")
print(f"Nilai Akhir\t : {nilai_akhir}")

if  nilai_akhir >= 90:
    print("Grade\t\t : A")
elif  nilai_akhir >= 80:
    print("Grade\t\t : B")
elif  nilai_akhir >= 70:
    print("Grade\t\t : C")
elif  nilai_akhir >= 50:
    print("Grade\t\t : D")
elif  nilai_akhir >= 0:
    print("Grade\t\t : E")

if nilai_akhir >= 50:
    print("Katerangan\t : LULUS")
else:
    print("Keterangan\t : TIDAK LULUS")
