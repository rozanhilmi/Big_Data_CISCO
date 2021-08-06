hitung = 'kubus','balok','bola' 
for x in hitung :
  hitung = str(input('mau menghitung apa ?  (kubus/balok/bola) '))
  if hitung == 'kubus':
   sisi = int(input('sisinya berapa ? '))
   print()
   print('-------- KUBUS ---------')
   luas = 6*sisi*sisi
   keliling = 12*sisi
   volume = sisi*sisi*sisi
   print('luas kubus        = ', luas)
   print('keliling kubus    = ', keliling)
   print('keliling volume   = ', volume)
   print('--------------------------')
   tanya = str(input('Ingin coba menghitung lagi?  (iya/tidak) '))
   if tanya == 'iya':
    continue
   else :
     print('======================================================')
     print('       PROGRAM MENGHIUTNG BANGUN RUANG SELESAI        ')
     print('======================================================')
     break
  if hitung == 'balok':
   panjang  = int(input('panjangnya berapa ? '))
   lebar    = int(input('lebarnya berapa ? '))
   tinggi   = int(input('tingginya berapa ? '))
   print()
   print('----------- BALOK -----------')
   Luas     = 2*(panjang*lebar)+(panjang*tinggi)+(lebar*tinggi)
   Keliling = 4*(panjang+lebar+tinggi)
   volume   = panjang*lebar*tinggi
   print('luas balok     = ', Luas)
   print('Keliling balok = ', Keliling)
   print('volume balok   = ', volume)
   print('-----------------------------')
   tanya = str(input('Ingin coba menghitung lagi? (iya/tidak) '))
   if tanya == 'iya':
     continue
   else :
     print('======================================================')
     print('       PROGRAM MENGHIUTNG BANGUN RUANG SELESAI        ')
     print('======================================================')
     break
  if hitung == 'bola':
    r = int(input('jari-jarinya berapa ? '))
    print()
    print('----------- BOLA -----------')
    phi = 3.14
    luas = 4*phi*r*r
    keliling = 4/3*phi*r*r
    volume = 4/3*phi*r*r*r
    print('Luas balok     = ', luas)
    print('Keliling balok = ', keliling)
    print('Volume bola  fe= ', volume)
    print('----------------------------')
    tanya = str(input('Ingin coba menghitung lagi?  (iya/tidak) '))
    if tanya == 'iya':
     continue
    else :
     print('======================================================')
     print('       PROGRAM MENGHIUTNG BANGUN RUANG SELESAI        ')
     print('======================================================')
     break

