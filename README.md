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
git clone [https://github.com/USERNAME_KAMU/GHOST-OSINT](https://github.com/USERNAME_KAMU/GHOST-OSINT)
cd GHOST-OSINT
pip install -r requirements.txt
python main.py
```
### 2. Linux / Windows / macOS
​Pastikan sudah menginstal Python 3
```bash
git clone [https://github.com/USERNAME_KAMU/GHOST-OSINT](https://github.com/USERNAME_KAMU/GHOST-OSINT)
cd GHOST-OSINT
pip install requests phonenumbers
python main.py
