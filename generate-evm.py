from web3 import Web3
import os
from colorama import Fore, Style, init


init(autoreset=True)


CHECK_MARK = Fore.GREEN + "✔️" + Style.RESET_ALL
CROSS_MARK = Fore.RED + "❌" + Style.RESET_ALL


print(Fore.YELLOW + "========================================")
print(Fore.CYAN + "AUTHOR : ANAM BACTIAR")
print(Fore.MAGENTA + "THANKS TO : ANAM BACTIAR!")
print(Fore.BLUE + "GITHUB: https://github.com/bactiar291")
print(Fore.GREEN + "BUY COFFEE FOR ME : 0x648dce97a403468dfc02c793c2b441193fccf77b")
print(Fore.YELLOW + "========================================\n")

def create_wallet():
   
    web3 = Web3()

    try:
        
        account = web3.eth.account.create()

       
        print(Fore.GREEN + f"Alamat Dompet Baru: {account.address} " + CHECK_MARK)
        print(Fore.GREEN + f"Kunci Pribadi: {account._private_key.hex()} " + CHECK_MARK)

        
        with open("wallets.txt", "a") as file:
            file.write(f"Alamat Dompet: {account.address}\n")
            file.write(f"Kunci Pribadi: {account._private_key.hex()}\n")
            file.write("=====================================\n")

        print(Fore.GREEN + "Alamat dan kunci pribadi disimpan di 'wallets.txt'. Harap simpan kunci pribadi dengan aman!" + CHECK_MARK)

    except Exception as e:
        print(Fore.RED + "Gagal membuat dompet: " + str(e) + CROSS_MARK)

if __name__ == "__main__":
    jumlah_wallet = int(input(Fore.CYAN + "Masukkan jumlah dompet yang ingin dibuat: "))

    for i in range(jumlah_wallet):
        create_wallet()
        print(Fore.YELLOW + f"Dompet {i+1} berhasil dibuat.\n")
