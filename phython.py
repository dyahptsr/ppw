class AkunBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo  # Atribut private, hanya bisa diakses di dalam kelas

    def deposit(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil deposit {jumlah}. Saldo sekarang: {self.__saldo}")
        else:
            print("Jumlah deposit harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"Berhasil tarik {jumlah}. Saldo sekarang: {self.__saldo}")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")

    def cek_saldo(self):
        return self.__saldo

# Penggunaan
akun = AkunBank("Budi", 100000)
akun.deposit(50000)
akun.tarik(30000)
print("Saldo akhir:", akun.cek_saldo())
