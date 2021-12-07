import os 

print(50 * "=")
print("|\tSelamat Datang di ADYASKARA Hospital \t|")
print("|\tDiagnosa Penyakit              \t\t|")
print(50 * "=")
nama = input("Nama\t: ")
pilihan = input("Hello "+nama+ ",\nApakah Anda Ingin Melakukan Diagnosa ? (y/n) ")

os.system

while pilihan == "y":
    print("\nApakah Anda Merasakan Gejala Berikut Ini ? : ")
    print("1. Demam / Suhu Badan Tinggi ")
    print("2. Sakit Tenggorokan")
    print("3. Nyeri Dada Saat Bernafas atau Batuk ")
    print("4. Lemas ")
    diag1 = input("Jawab (y/n) : ")

    if diag1 == "y" :
        print("\nApakah Anda Juga Merasakan Gejala Berikut Ini ? : ")
        print("1. Hilang Nafsu Makan")
        print("2. Penurunan Berat Badan")
        print("3. Batuk Berlangsung lama")
        diag2 = input("Jawab (y/n) : ")

        if diag2 == "y" :
            print("\nHello " +nama+ ", Hasil Awal Diagnosa Kamu adalah : ")
            print("Gejala Tuberkulosis, Segeralah ke Dokter")
        elif diag2 == "n" :
            print("\nApakah Anda Merasakan Gejala Berikut Ini ? : ")
            print("1. Nyeri Sendiri")
            print("2. Ruam-Ruam")
            print("3. Sakit Kepala")
            print("4. Mual dan Muntah")
            diag3 = input("Jawab (y/n) : ")

            if diag3 == "y" :
                print("\nHello " +nama+ ", Hasil Awal Diagnosa Kamu adalah : ")
                print("Gejala Demam Berdarah, Segeralah ke Dokter")
            elif diag3 == "n" :
                print("\nHello "+nama+ ", Anda Sepertinya Butuh Istirahat Yang Cukup")
            else :
                print("\nHello "+nama+ ", Anda Sepertinya Tidak Mau Berobat")
        else :
            print("\nHello "+nama+ ", Anda Sepertinya Tidak Mau Berobat")
    elif diag1 == "n" :
        print("\nHello "+nama+ ", Anda Sepertinya Butuh Jalan-Jalan")
    else :
        print("\nHello "+nama+ ", Anda Sepertinya Tidak Mau Berobat")
    print(50 * "=")
    pilihan = input("Hello "+nama+ ",\nApakah Anda Ingin Melakukan Diagnosa Lagi ? (y/n)")
    
    if pilihan == "y" :
        os.system
        print(50 * "=")
        print("|\tSelamat Datang di ADYASKARA Hospital \t|")
        print("|\tDeteksi Maag dan Tuberkulosis \t\t|")
        print(50 * "=")
    else : 
        print(20 * "=", "Terima Kasih", 20 * "=")


