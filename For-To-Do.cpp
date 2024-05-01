#include <iostream>

int main() {
    int total = 0;
    for (int i = 1; i <= 10; ++i) {
        total += i; // Menambahkan i ke total
    }
    std::cout << "Jumlah dari 1 hingga 10 adalah: " << total << std::endl;
    return 0;
}
