def caesar_encrypt(plainteks, k):
    cipherteks = ""
    for char in plainteks:
        if char.isalpha():
            # Tentukan batas awal ASCII ('A' untuk huruf kapital, 'a' untuk huruf kecil)
            start = ord('A') if char.isupper() else ord('a')
            # Rumus enkripsi: c = (p + k) mod 26
            c = (ord(char) - start + k) % 26
            cipherteks += chr(c + start)
        else:
            # Karakter selain huruf (spasi, angka, simbol) dibiarkan tetap
            cipherteks += char
    return cipherteks

def caesar_decrypt(cipherteks, k):
    plainteks = ""
    for char in cipherteks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Rumus dekripsi: p = (c - k) mod 26
            c = (ord(char) - start - k) % 26
            plainteks += chr(c + start)
        else:
            plainteks += char
    return plainteks

# Program Utama (Menu Interaktif)
if __name__ == "__main__":
    print("=== APLIKASI CAESAR CIPHER ===")
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == '1':
        pesan = input("Masukkan pesan (plainteks): ")
        kunci = int(input("Masukkan jumlah pergeseran kunci (0-25): "))
        hasil = caesar_encrypt(pesan, kunci)
        print(f"Hasil Enkripsi (Cipherteks): {hasil}")
    elif pilihan == '2':
        pesan = input("Masukkan pesan tersandi (cipherteks): ")
        kunci = int(input("Masukkan jumlah pergeseran kunci (0-25): "))
        hasil = caesar_decrypt(pesan, kunci)
        print(f"Hasil Dekripsi (Plainteks): {hasil}")
    else:
        print("Pilihan menu tidak valid!")