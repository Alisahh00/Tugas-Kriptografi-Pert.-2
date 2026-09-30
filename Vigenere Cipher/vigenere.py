def vigenere_encrypt(plainteks, kunci):
    cipherteks = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in plainteks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            k_shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            
            c = (ord(char) - start + k_shift) % 26
            cipherteks += chr(c + start)
            kunci_index += 1
        else:
            cipherteks += char
            
    return cipherteks

def vigenere_decrypt(cipherteks, kunci):
    plainteks = ""
    kunci = kunci.upper()
    kunci_index = 0
    
    for char in cipherteks:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            k_shift = ord(kunci[kunci_index % len(kunci)]) - ord('A')
            
            c = (ord(char) - start - k_shift) % 26
            plainteks += chr(c + start)
            kunci_index += 1
        else:
            plainteks += char
            
    return plainteks

# Program Utama (Menu Interaktif)
if __name__ == "__main__":
    print("=== APLIKASI VIGENERE CIPHER ===")
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == '1':
        pesan = input("Masukkan pesan (plainteks): ")
        kunci = input("Masukkan kata kunci (string): ")
        hasil = vigenere_encrypt(pesan, kunci)
        print(f"Hasil Enkripsi (Cipherteks): {hasil}")
    elif pilihan == '2':
        pesan = input("Masukkan pesan tersandi (cipherteks): ")
        kunci = input("Masukkan kata kunci (string): ")
        hasil = vigenere_decrypt(pesan, kunci)
        print(f"Hasil Dekripsi (Plainteks): {hasil}")
    else:
        print("Pilihan menu tidak valid!")