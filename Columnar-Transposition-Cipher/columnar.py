def columnar_encrypt(plainteks, kunci):
    # Hilangkan spasi pada plainteks (opsional, agar matriks pas)
    plainteks = plainteks.replace(" ", "")
    panjang_kunci = len(kunci)
    
    # Tambahkan padding 'X' jika panjang teks tidak pas dengan kolom
    while len(plainteks) % panjang_kunci != 0:
        plainteks += 'X'
        
    # Menyusun teks ke dalam bentuk grid/tabel baris
    grid = [plainteks[i:i+panjang_kunci] for i in range(0, len(plainteks), panjang_kunci)]
    
    # Membaca kolom berdasarkan urutan abjad dari kata kunci
    # Mengurutkan indeks kunci berdasarkan abjad
    urutan_kunci = sorted(list(enumerate(kunci)), key=lambda x: x[1])
    
    cipherteks = ""
    for index, _ in urutan_kunci:
        for baris in grid:
            cipherteks += baris[index]
            
    return cipherteks

def columnar_decrypt(cipherteks, kunci):
    panjang_kunci = len(kunci)
    panjang_teks = len(cipherteks)
    jumlah_baris = panjang_teks // panjang_kunci
    
    urutan_kunci = sorted(list(enumerate(kunci)), key=lambda x: x[1])
    
    # Memetakan kembali cipherteks ke dalam kolom
    kolom = {}
    indeks_sekarang = 0
    for index, _ in urutan_kunci:
        kolom[index] = cipherteks[indeks_sekarang:indeks_sekarang + jumlah_baris]
        indeks_sekarang += jumlah_baris
        
    # Menyusun kembali baris menjadi plainteks
    grid = [''] * jumlah_baris
    for i in range(jumlah_baris):
        for j in range(panjang_kunci):
            grid[i] += kolom[j][i]
            
    plainteks = "".join(grid)
    return plainteks

# Program Utama (Menu Interaktif)
if __name__ == "__main__":
    print("=== APLIKASI COLUMNAR TRANSPOSITION CIPHER ===")
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == '1':
        pesan = input("Masukkan pesan (plainteks): ")
        kunci = input("Masukkan kata kunci (string): ")
        hasil = columnar_encrypt(pesan, kunci)
        print(f"Hasil Enkripsi (Cipherteks): {hasil}")
    elif pilihan == '2':
        pesan = input("Masukkan pesan tersandi (cipherteks): ")
        kunci = input("Masukkan kata kunci (string): ")
        hasil = columnar_decrypt(pesan, kunci)
        print(f"Hasil Dekripsi (Plainteks): {hasil}")
    else:
        print("Pilihan menu tidak valid!")