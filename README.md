# auto-generate-evm
# EVM Wallet Generator

Sebuah skrip Python sederhana yang digunakan untuk membuat dompet Ethereum Virtual Machine (EVM) secara otomatis, lengkap dengan alamat dompet dan kunci pribadi. Skrip ini menggunakan `Web3` untuk membuat dompet dan `colorama` untuk menampilkan pesan berwarna di terminal.

## Fitur

- Membuat beberapa dompet EVM sekaligus.
- Menyimpan alamat dompet dan kunci pribadi ke file `wallets.txt`.
- Menampilkan status sukses atau gagal dalam format berwarna di terminal.
- Informasi akun ditampilkan dalam format yang aman dan mudah diakses.

## Persyaratan

Proyek ini memerlukan Python 3.x dan beberapa pustaka Python yang dapat diinstal melalui `pip`. Pastikan untuk menginstal dependensi terlebih dahulu dengan menjalankan perintah berikut.

## Cara Install

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/bactiar291/generate-evm.git
   cd generate-evm
   ```
Install dependensi:

Gunakan pip untuk menginstal pustaka yang dibutuhkan dari file requirements.txt:

```bash
Salin kode
pip install -r requirements.txt
```
Pustaka yang dibutuhkan:

web3
colorama

Cara Penggunaan
Jalankan skrip dengan perintah berikut di terminal:

```bash
Salin kode
python generate-evm.py
```
Masukkan jumlah dompet:
Setelah menjalankan skrip, Anda akan diminta untuk memasukkan jumlah dompet yang ingin dibuat. Misalnya, jika Anda ingin membuat 5 dompet, cukup masukkan angka 5.

Output:
Alamat dompet baru dan kunci pribadi akan dicetak di terminal.
Data akan disimpan ke dalam file wallets.txt di direktori yang sama.

Contoh:
Salin kode
Masukkan jumlah dompet yang ingin dibuat: 3
Alamat Dompet Baru: 0x1234567890ABCDEF1234567890ABCDEF12345678 ✔️
Kunci Pribadi: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890 ✔️
Alamat dan kunci pribadi disimpan di 'wallets.txt'. Harap simpan kunci pribadi dengan aman! ✔️
Dompet 1 berhasil dibuat.
Kontributor
Author: ANAM BACTIAR
GitHub: github.com/bactiar291
Lisensi
Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail lebih lanjut.

