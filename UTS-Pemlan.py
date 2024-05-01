"""================
Perpustakaan Python
================"""
import UProgram # untuk mengambil file di list-program.py
import os
import sys

def main():
    while True: # Perulangan
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input(
        "\033	       +====== Program UTS ======+ \n"
        "\033	       | 1. Program For-To-Do    | \n"
        "\033	       | 2. Program While-Do     | \n"
        "\033	       | 3. Program Repeat-Until | \n"
        "\033	       +=========================+ \n\n"
        "\033[094m┌──("
        "\033[1m"
        "\033[091mUTSPemlan㉿Afrizal"
        "\033[0m"
        "\033[094m)-["
        "\033[1m"
        "\033[37mPilih Program"
        "\033[094m]\n"
        "\033[094m└─"
        "\033[1m"
        "\033[091m> "
        "\033[0m"))
        
        if choice >= 1 and choice <= 3:
            UProgram.run_program(choice)
        if choice >= 4:
            input("Mohon Masukan Angka yang benar")
            
if __name__ == "__main__":
    main()
