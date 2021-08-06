# Menghitung jam yang akan datang

jam = int(input("Jam berapa: "))
menit = int(input("Menit ke berapa: "))
durasi = int(input("Durasi tambahan waktu dalam menit: "))
menit = menit + durasi 
jam = jam + menit // 60 
menit = menit % 60 
jam = jam % 24 
print(jam, ":", menit, sep='')
