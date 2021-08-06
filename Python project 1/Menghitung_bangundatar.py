hitung = 'persegi','persegi panjang'
for x in hitung :
  hitung = str(input('mau menghitung apa ?  (persegi/persegi panjang) '))
  if hitung == 'persegi':
   sisi = int(input('sisinya berapa ? '))
   print()
   print('-------- PERSEGI ---------')
   luas = sisi*sisi
   keliling = 4*sisi
   print('luas persegi     = ', luas)
   print('keliling persegi = ', keliling)
   print('--------------------------')
   tanya = str(input('Ingin menhitung persegi atau persegi panjang lagi?  (iya/tidak) '))
   if tanya == 'iya':
    continue
   else :
     print('======================================================')
     print('PROGRAM MENGHIUTNG PERSEGI DAN PERSEGI PANJANG SELESAI')
     print('======================================================')
     break
  if hitung == 'persegi panjang':
   panjang = int(input('panjangnya berapa ? '))
   lebar   = int(input('lebarnya berapa ? '))
   print()
   print('------ PERSEGI PANJANG ------')
   Luas = panjang*lebar
   Keliling = 2*(panjang+lebar)
   print('luas persegi panjang     = ', Luas)
   print('Keliling persegi panjang = ', Keliling)
   print('-----------------------------')
   tanya = str(input('Ingin menhitung persegi atau persegi panjang lagi?  (iya/tidak) '))
   if tanya == 'iya':
     continue
   else :
     print('======================================================')
     print('PROGRAM MENGHIUTNG PERSEGI DAN PERSEGI PANJANG SELESAI')
     print('======================================================')
     break
