# 🐉 GHOST-OSINT v2.0
**Information Gathering Tool by SPY-E & 123Tool**

GHOST-OSINT adalah alat intelijen sumber terbuka (OSINT) yang dirancang untuk membantu researcher keamanan siber dalam mengumpulkan informasi publik secara otomatis.

## ✨ Fitur Utama
- **IP Tracker**: Melacak lokasi, ISP, dan koordinat IP Address.
- **Phone Tracker**: Mengetahui provider dan lokasi pendaftaran nomor telepon.
- **Username Tracker**: Mencari ketersediaan username di berbagai media sosial populer menggunakan teknik *Multithreading* (sangat cepat).
- **Cross-Platform**: Support Termux, Linux, Windows (CMD/PowerShell), dan macOS.

## 🚀 Instalasi

### 1. Termux (Android)
```bash
pkg update && pkg upgrade
pkg install python git
git clone [https://github.com/123tool/GHOST-OSINT-v2.0.git](https://github.com/123tool/GHOST-OSINT-v2.0.git)
cd GHOST-OSINT-v2.0
pip install -r requirements.txt
python main.py
```
### 2. Linux / Windows / macOS
​Pastikan sudah menginstal Python 3
```bash
git clone [https://github.com/123tool/GHOST-OSINT-v2.0.git](https://github.com/123tool/GHOST-OSINT-v2.0.git)
cd GHOST-OSINT-v2.0
pip install requests phonenumbers
python main.py
```

## 📖 Cara Penggunaan
​Jalankan script dengan perintah python main.py.
​Pilih opsi menu (1-3).
​Masukkan target (IP, Nomor HP, atau Username).
​Hasil akan muncul secara real-time.

## ​⚠️ Disclaimer
​Alat ini dibuat untuk tujuan edukasi dan penelitian keamanan (OSINT). Pengembang (SPY-E & 123Tool) tidak bertanggung jawab atas penyalahgunaan alat ini untuk tindakan ilegal.

***​Powered by SPY-E & 123Tool***
