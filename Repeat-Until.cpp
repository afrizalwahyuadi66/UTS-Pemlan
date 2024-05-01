#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    std::srand(std::time(nullptr)); // Inisialisasi random number generator
    int total = 0;
    
    while (true) { // Loop terus menerus
        int number = std::rand() % 10 + 1; // Mendapatkan angka acak antara 1 dan 10
        total += number; // Menambahkan angka ke total
        std::cout << "Menambahkan " << number << ", total saat ini: " << total << std::endl;
        
        if (total > 50) { // Jika total melebihi 50, keluar dari loop
            break;
        }
    }
    
    return 0;
}
