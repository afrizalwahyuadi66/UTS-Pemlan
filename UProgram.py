import sys
import os
import random # Untuk Pemrograman Repeat-Until di program_3()

def run_program(choice):
    if choice == 1:
        program_1()
    elif choice == 2:
        program_2()
    elif choice == 3:
        program_3()

# Program 1 =========================================================
def program_1():
    print("\033[01m+==== PROGRAM For-To-Do ====+"
          "\033[00m")
    
    # Menghitung jumlah angka dari 1 hingga 10 menggunakan loop for
    total = 0
    for i in range(1, 11):
        total += i  # Menambahkan i ke total
    print("Jumlah dari 1 hingga 10 adalah:", total)
    print("\033[01m+===========================+"
          "\033[00m")
    print()
    input("\033 Tekan "
          "\033[01m"
          "\033[094m[Enter] "
          "\033[00m"
          "\033 Untuk Kembali"
          "\033[00m")

# Program 2 ======================================================
def program_2():
    print("\033[01m+==== PROGRAM While-Do ====+"
          "\033[00m")
    
    # Menampilkan angka dari 1 hingga 10 menggunakan loop while
    count = 1
    while count <= 10:
        print(count)  # Mencetak nilai count
        count += 1  # Menambahkan count dengan 1
    print("\033[01m+==========================+"
          "\033[00m")
    print()
    input("\033 Tekan "
          "\033[01m"
          "\033[094m[Enter] "
          "\033[00m"
          "\033 Untuk Kembali"
          "\033[00m")

# Program 3 ===================================================================
def program_3():
    print("\033[01m+==== PROGRAM Repeat-Until ====+"
          "\033[00m")
    # Menambahkan angka acak sampai totalnya melebihi 50
    total = 0
    while True:  # Loop terus menerus
        number = random.randint(1, 10)  # Mendapatkan angka acak antara 1 dan 10
        total += number  # Menambahkan angka ke total
        print(f"Menambahkan {number}, total saat ini: {total}")
        if total > 50:  # Jika total melebihi 50, keluar dari loop
            break
    print("\033[01m+==============================+"
          "\033[00m")
    print()
    input("\033 Tekan "
          "\033[01m"
          "\033[094m[Enter] " 
          "\033[00m"
          "\033 Untuk Kembali"
          "\033[00m")
