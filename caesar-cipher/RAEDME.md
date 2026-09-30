-Caesar Cipher adalah salah satu algoritma enkripsi klasik paling sederhana dan tertua yang menggunakan teknik substitusi abjad tunggal.   Cara kerjanya adalah dengan mengganti setiap huruf pada pesan asli (plainteks) dengan huruf lain yang letaknya digeser sejauh k langkah di dalam urutan alfabet. 

-Enkripsi (Pesan ke Cipherteks):c = (p + k) (mod 26)
(Setiap huruf digeser ke kanan sejauh nilai kunci k).  
-Dekripsi (Cipherteks ke Pesan Asli):p = (c - k) (mod 26)
(Setiap huruf digeser kembali ke kiri sejauh nilai kunci k). 

- Hasil Pengujian Program (Testing)Berdasarkan hasil uji coba pada terminal Python:Plainteks: "apa kabar" dengan kunci pergeseran 8 berhasil diubah menjadi Cipherteks: "ixi sijiz".   Proses sebaliknya (dekripsi) juga berhasil mengembalikan pesan tersandi ke bentuk plainteks aslinya dengan akurat.
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/cfd7911d-7939-4029-9d6c-b802b2b8a41f" />

